"""Loads app/seed/cases.py into the case_library_entries table.

Upserts by (phrase_or_concept, region, category) so it's safe to re-run
after editing/adding entries to CASES.

Usage:
    python -m app.seed.seed_db
"""

from datetime import date, datetime

from app.db import SessionLocal
from app.models.case import CaseLibraryEntry
from app.seed.cases import CASES


def _parse_date(value: str | None) -> date | None:
    if not value:
        return None
    if len(value) == 7:  # YYYY-MM
        value = f"{value}-01"
    return datetime.strptime(value, "%Y-%m-%d").date()  # noqa: DTZ007 (date-only, tz irrelevant)


def seed() -> None:
    db = SessionLocal()
    inserted = 0
    updated = 0
    try:
        for case in CASES:
            existing = (
                db.query(CaseLibraryEntry)
                .filter(
                    CaseLibraryEntry.phrase_or_concept == case["phrase_or_concept"],
                    CaseLibraryEntry.region == case["region"],
                    CaseLibraryEntry.category == case["category"],
                )
                .one_or_none()
            )

            fields = {
                "industry_tags": case.get("industry_tags", []),
                "content_type_tags": case.get("content_type_tags", []),
                "description": case["description"],
                "source_url": case["source_url"],
                "date_occurred": _parse_date(case.get("date_occurred")),
                "severity_baseline": case["severity_baseline"],
                "active": case.get("active", True),
            }

            if existing is None:
                db.add(
                    CaseLibraryEntry(
                        phrase_or_concept=case["phrase_or_concept"],
                        region=case["region"],
                        category=case["category"],
                        **fields,
                    )
                )
                inserted += 1
            else:
                for key, value in fields.items():
                    setattr(existing, key, value)
                updated += 1

        db.commit()
    finally:
        db.close()

    print(f"Seeded case library: {inserted} inserted, {updated} updated.")


if __name__ == "__main__":
    seed()
