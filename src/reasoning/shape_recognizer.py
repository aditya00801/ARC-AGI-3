from src.core.object import ARCObject


class ShapeRecognizer:
    """
    Identifies the geometric shape of an ARCObject.
    """

    @staticmethod
    def recognize(obj: ARCObject) -> str:
        """
        Recognize the basic geometric shape of an object.

        Returns:
            - single_pixel
            - horizontal_line
            - vertical_line
            - square
            - rectangle
            - irregular
        """

        # Single pixel
        if obj.area == 1:
            return "single_pixel"

        # Horizontal line
        if obj.height == 1:
            return "horizontal_line"

        # Vertical line
        if obj.width == 1:
            return "vertical_line"

        # Filled square
        if (
            obj.width == obj.height
            and obj.area == obj.width * obj.height
        ):
            return "square"

        # Filled rectangle
        if obj.area == obj.width * obj.height:
            return "rectangle"

        # Anything else
        return "irregular"