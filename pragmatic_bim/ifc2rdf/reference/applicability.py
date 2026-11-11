"""Parse and evaluate pragmaticBIM Reference ``applicability`` expressions.

Grammar (as used in ``elements/*.yaml``)::

    expr   := term (OR term)*
    term   := factor (AND factor)*
    factor := "(" expr ")" | clause
    clause := NAME "=" VALUE      # comparison
            | NAME                # existence: attribute or property is set

``NAME`` is an IFC attribute (``ObjectType``), a property searched in every property
set (``IsExternal``), ``Pset.Property``, or ``entity_ifc2x3`` / ``entity_ifc4`` /
``entity_ifc4_3`` for the IFC class. ``VALUE`` is a bare token or a double-quoted string.

Ported from ``pragmaticBIM-reference/catalog/applicability.py`` with existence clauses
and a match score: the number of clauses satisfied by the matching branch, used to
prefer the most specific element definition.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

ENTITY_ATTRIBUTES = ("entity_ifc2x3", "entity_ifc4", "entity_ifc4_3")


@dataclass(frozen=True)
class Clause:
    attribute: str
    value: str | None
    """Expected value; None for an existence clause."""


@dataclass(frozen=True)
class Operation:
    operator: str
    """``AND`` or ``OR``."""
    operands: tuple["Expression", ...]


Expression = Clause | Operation


def parse(text: str) -> Expression:
    parser = _Parser(_tokenize(text))
    expression = parser.parse_or()
    if parser.peek() is not None:
        raise ValueError(f"trailing token {parser.peek()!r} in {text!r}")
    return expression


def clauses(expression: Expression) -> list[Clause]:
    if isinstance(expression, Clause):
        return [expression]
    return [c for operand in expression.operands for c in clauses(operand)]


def entity_classes(expression: Expression) -> set[str]:
    """IFC classes named by ``entity_ifc*`` clauses (empty when none are)."""
    return {c.value for c in clauses(expression) if c.attribute in ENTITY_ATTRIBUTES and c.value}


Resolver = Callable[[Clause], bool]


def evaluate(expression: Expression, holds: Resolver) -> tuple[bool, int]:
    """``(matched, score)``; ``score`` counts the clauses of the best matching branch."""
    if isinstance(expression, Clause):
        result = holds(expression)
        return result, int(result)
    results = [evaluate(operand, holds) for operand in expression.operands]
    if expression.operator == "AND":
        if all(matched for matched, _ in results):
            return True, sum(score for _, score in results)
        return False, 0
    scores = [score for matched, score in results if matched]
    return (True, max(scores)) if scores else (False, 0)


def clause_applies_to_schema(attribute: str, file_schema: str, has_ifc4x3_clause: bool) -> bool:
    """Whether an ``entity_ifc*`` clause applies to a file of ``file_schema``.

    IFC4X3 files also accept ``entity_ifc4`` clauses when the expression has no
    ``entity_ifc4_3`` clause, because most reference elements only name IFC4 classes.
    """
    schema = file_schema.upper()
    if attribute == "entity_ifc2x3":
        return schema.startswith("IFC2X3")
    if attribute == "entity_ifc4_3":
        return schema.startswith("IFC4X3")
    if attribute == "entity_ifc4":
        if schema.startswith("IFC4X3"):
            return not has_ifc4x3_clause
        return schema.startswith("IFC4")
    return False


class _Parser:
    def __init__(self, tokens: list[Any]) -> None:
        self.tokens = tokens
        self.index = 0

    def peek(self) -> Any:
        return self.tokens[self.index] if self.index < len(self.tokens) else None

    def parse_or(self) -> Expression:
        operands = [self.parse_and()]
        while self.peek() == "OR":
            self.index += 1
            operands.append(self.parse_and())
        return operands[0] if len(operands) == 1 else Operation("OR", tuple(operands))

    def parse_and(self) -> Expression:
        operands = [self.parse_factor()]
        while self.peek() == "AND":
            self.index += 1
            operands.append(self.parse_factor())
        return operands[0] if len(operands) == 1 else Operation("AND", tuple(operands))

    def parse_factor(self) -> Expression:
        token = self.peek()
        if token == "(":
            self.index += 1
            expression = self.parse_or()
            if self.peek() != ")":
                raise ValueError("missing closing parenthesis")
            self.index += 1
            return expression
        if isinstance(token, Clause):
            self.index += 1
            return token
        raise ValueError(f"unexpected token {token!r}")


def _tokenize(text: str) -> list[Any]:
    tokens: list[Any] = []
    index, length = 0, len(text)
    while index < length:
        char = text[index]
        if char.isspace():
            index += 1
            continue
        if char in "()":
            tokens.append(char)
            index += 1
            continue
        if _keyword_at(text, index, "AND"):
            tokens.append("AND")
            index += 3
            continue
        if _keyword_at(text, index, "OR"):
            tokens.append("OR")
            index += 2
            continue
        start = index
        while index < length and (text[index].isalnum() or text[index] in "._"):
            index += 1
        attribute = text[start:index]
        if not attribute:
            raise ValueError(f"expected attribute at {text[index:index + 24]!r}")
        if index >= length or text[index] != "=":
            tokens.append(Clause(attribute, None))
            continue
        index += 1
        if index < length and text[index] == '"':
            end = text.find('"', index + 1)
            if end < 0:
                raise ValueError(f"unterminated quote in {text!r}")
            value = text[index + 1 : end]
            index = end + 1
        else:
            start = index
            while index < length and not text[index].isspace() and text[index] not in "()":
                index += 1
            value = text[start:index]
        tokens.append(Clause(attribute, value))
    return tokens


def _keyword_at(text: str, index: int, keyword: str) -> bool:
    if not text.startswith(keyword, index):
        return False
    before_ok = index == 0 or not (text[index - 1].isalnum() or text[index - 1] == "_")
    end = index + len(keyword)
    after_ok = end >= len(text) or not (text[end].isalnum() or text[end] in "_.=")
    return before_ok and after_ok
