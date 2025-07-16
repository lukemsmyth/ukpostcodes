"""This module contains the validate() function (main api of the library). As well as a numbe of utility functions."""

import re
from ukpostcodes.constants import (
    _POSTCODE_REGEX_1,
    _POSTCODE_REGEX_2,
    _POSTCODE_REGEX_3,
)


def validate(postcode: str) -> bool:
    """Validates a postcode against three possible valid patterns.

    Args:
        postcode: postcode string to validate

    Returns:
          Whether the string is a valid UK postcode.

    """
    postcode = postcode.upper()
    return any(
        [
            re.match(_POSTCODE_REGEX_1, postcode),
            re.match(_POSTCODE_REGEX_2, postcode),
            re.match(_POSTCODE_REGEX_3, postcode),
        ]
    )
