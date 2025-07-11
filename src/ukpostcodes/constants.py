"""This module contains constants which are used throughout the library"""

# regular expressions taken from section D.2 of this UK Government standards document: https://assets.publishing.service.gov.uk/media/632b07338fa8f53cb77ef6b8/WS02_LRS_Web_Services_Interface_Specification_v6.4.pdf
_POSTCODE_REGEX_1 = r"^[A-Z]{1,2}[0-9R][0-9A-Z]? ?[0-9][ABDEFGHJLNPQRSTUWXYZ]{2}$"
_POSTCODE_REGEX_2 = r"^BFPO ?[0-9]{1,4}$"
_POSTCODE_REGEX_3 = r"^([AC-FHKNPRTV-Y]\d{2}|D6W)? ?[0-9AC-FHKNPRTV-Y]{4}$"
