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