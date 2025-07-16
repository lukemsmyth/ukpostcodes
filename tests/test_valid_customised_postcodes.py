from ukpostcodes import validate

VALID_CUSTOMISED_POSTCODE_EXAMPLES = ["BX1 1LT", "B1 1HQ", "CF10 1BH", "SW1P 3EU"]


# Test valid customised postcodes
def test_validate_returns_true_for_valid_customised_postcode():
    assert all([validate(postcode) for postcode in VALID_CUSTOMISED_POSTCODE_EXAMPLES])


def test_validate_returns_true_for_valid_customised_postcode_without_whitespace():
    assert all(
        [
            validate(postcode.replace(" ", ""))
            for postcode in VALID_CUSTOMISED_POSTCODE_EXAMPLES
        ]
    )


def test_validate_returns_true_for_valid_customised_postcode_in_lowercase():
    assert all(
        [validate(postcode.lower()) for postcode in VALID_CUSTOMISED_POSTCODE_EXAMPLES]
    )
