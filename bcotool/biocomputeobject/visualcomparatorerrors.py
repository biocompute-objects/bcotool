
class VisualComparatorError(Exception):
    """
    Visual Comparator base class for exceptions.  Can be used as a generic exception
    """


class RGBNotInRangeError(VisualComparatorError):
    """
    Raised when any RGB value is outside the expected 0 - 255 range.
    """

    def __init__(self, rgb: str, value: int):
        self.message = "Undefined error setting RGB color."
        if value < 0:
            self.message = "The value for {} is below 0.  A value is expected to be between 0 and 255."
        elif value > 255:
            self.message = "The value for {} is above 255.  A value is expected to be between 0 and 255."
        super().__init__(self.message)

class ValueOutOfRange(VisualComparatorError):
    """
    Generic value out of range error for the Visual Comparator
    """

    def __init__(self, message="The value entered here is outside of the range of accepted values."):
        self.message = message
        super().__init__(self.message)
