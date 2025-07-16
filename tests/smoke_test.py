from ukpostcodes import validate

VALID_POSTCODE = "DE7 8HQ"
INVALID_POSTCODE = "INVALID_POSTCODE"


def test_validate_returns_true_for_valid_postcode():
    assert validate(VALID_POSTCODE)


def test_validate_returns_false_for_invalid_postcode():
    assert not validate(INVALID_POSTCODE)


def test_validate_returns_true_for_valid_postcode_without_whitespace():
    assert validate("DE78HQ")


def test_validate_returns_true_for_valid_postcode_in_lowercase():
    assert validate("de78hq")

def test_validate_returns_true_for_valid_xx_postcode():
    xx_postcode = "XX40 4AA"
    assert validate(xx_postcode)