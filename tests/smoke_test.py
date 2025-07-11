from ukpostcodes import validate

VALID_POSTCODE = "DE7 8HQ"
INVALID_POSTCODE = "INVALID_POSTCODE"


def test_validate_returns_true_for_valid_postcode():
    assert validate(VALID_POSTCODE)


def test_validate_returns_false_for_invalid_postcode():
    assert not validate(INVALID_POSTCODE)
