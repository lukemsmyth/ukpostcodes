from ukpostcodes import validate

VALID_GEOGRAPHIC_POSTCODE_EXAMPLES = [
    "CR2 6XH",
    "DN55 1PT",
    "M1 1AE",
    "B33 8TH",
    "W1A 0AX",
    "EC1A 1BB",
]


# Test valid geographic postcodes
def test_validate_returns_true_for_valid_geographic_postcode():
    assert all([validate(postcode) for postcode in VALID_GEOGRAPHIC_POSTCODE_EXAMPLES])


def test_validate_returns_true_for_valid_geographic_postcode_without_whitespace():
    assert all(
        [
            validate(postcode.replace(" ", ""))
            for postcode in VALID_GEOGRAPHIC_POSTCODE_EXAMPLES
        ]
    )


def test_validate_returns_true_for_valid_geographic_postcode_in_lowercase():
    assert all(
        [validate(postcode.lower()) for postcode in VALID_GEOGRAPHIC_POSTCODE_EXAMPLES]
    )
