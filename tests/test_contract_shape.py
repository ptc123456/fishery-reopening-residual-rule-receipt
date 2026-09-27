from pathlib import Path


SOURCE = Path(__file__).parents[1] / "contracts" / "fishery_reopening_residual_rule_receipt.py"
TEXT = SOURCE.read_text(encoding="utf-8")


def test_public_lifecycle_and_fail_closed_terms_are_present():
    for name in ("create_notice", "seal_notice", "assess_profile", "supersede_notice",
                 "get_assessment", "is_harvest_open", "get_residual_rights"):
        assert f"def {name}(" in TEXT
    for term in ("UNRESOLVED", "CLOSED_WITH_RESIDUAL", "PRE_CLOSURE_COLD_STORAGE",
                 "OPEN_WHILE_SECTOR_OPEN", "eq_principle.strict_eq", "nondet.web.render"):
        assert term in TEXT
