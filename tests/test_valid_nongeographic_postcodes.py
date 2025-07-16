from ukpostcodes import validate


VALID_NON_GEOGRAPHIC_POSTCODE_EXAMPLES = ["XX10 1FF", "XX20 1BF", "XX20 1FF"]


# Test valid non-geographic postcodes
def test_validate_returns_true_for_valid_nongeographic_postcode():
    assert all(
        [validate(postcode) for postcode in VALID_NON_GEOGRAPHIC_POSTCODE_EXAMPLES]
    )


def test_validate_returns_true_for_valid_nongeographic_postcode_without_whitespace():
    assert all(
        [
            validate(postcode.replace(" ", ""))
            for postcode in VALID_NON_GEOGRAPHIC_POSTCODE_EXAMPLES
        ]
    )


def test_validate_returns_true_for_valid_nongeographic_postcode_in_lowercase():
    assert all(
        [
            validate(postcode.lower())
            for postcode in VALID_NON_GEOGRAPHIC_POSTCODE_EXAMPLES
        ]
    )
