from ukpostcodes import validate


# Test invalid strings
def test_validate_returns_false_for_alphanumeric_string_of_length_greater_than_8():
    s = "ABCD12345"
    assert not validate(s)


def test_validate_returns_false_for_alphanumeric_string_of_length_less_than_6():
    s = "AB123"
    assert not validate(s)


def test_validate_returns_false_for_non_alphanumeric_string():
    s = "BX1-1LT"
    assert not validate(s)
