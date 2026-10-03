"""Python bindings for the pragmatic BIM data contract.

``models`` holds the generated LinkML Pydantic classes; ``taxonomy`` resolves the
SKOS classification codes those classes reference.

    from pragmatic_bim import taxonomy
    from pragmatic_bim.models import Company, Classification

    Company(id="co-1", content_kind="agent", name="Foo AG", classifications=[
        Classification(classification_scheme=taxonomy.COMPANY_SECTOR,
                       classification_code="SEC-BAU-CLI-GC")])
"""

from __future__ import annotations

from pragmatic_bim import models, taxonomy

__all__ = ["models", "taxonomy", "__version__"]

__version__ = "1.0.6"
