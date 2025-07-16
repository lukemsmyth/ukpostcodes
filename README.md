# `ukpostcodes`

This library provides functionality for checking whether a string is a valid UK postcode.

# Usage

```python
from ukpostcodes import validate

try:
    valid_postcode_str = "DE7 8HQ"
    assert validate(valid_postcode_str)
except AssertionError as e:
    print(f"'{valid_postcode_str}' is invalid")

try:
    invalid_postcode_str = "some invalid string"
    assert validate(invalid_postcode_str)
except AssertionError as e:
    print(f"'{invalid_postcode_str}' is invalid")

"""Output:
'some invalid string' is invalid
"""
```


# Validation Logic

## Regular Expressions

The validation is performed by checking against the regular expressions in `ukpostcodes.constants`. These regular expressions are defined in a [UK government standards document](https://assets.publishing.service.gov.uk/media/632b07338fa8f53cb77ef6b8/WS02_LRS_Web_Services_Interface_Specification_v6.4.pdf).

## `validate()` function

The `validate()` function *will* return `True` when passed an otherwise valid string which:
- does not have a whitespace separating the inward and outward codes
- contains lower case letters

# Tests

To run the tests:
```shell
uv run pytest
```