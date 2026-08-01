from src.core.object import ARCObject


class ObjectComparator:
    """
    Compares two ARC objects and reports their differences.
    """

    @staticmethod
    def compare(obj1: ARCObject, obj2: ARCObject) -> dict:
        return {
            "color_changed": obj1.color != obj2.color,
            "shape_changed": obj1.shape != obj2.shape,
            "area_changed": obj1.area != obj2.area,
            "width_changed": obj1.width != obj2.width,
            "height_changed": obj1.height != obj2.height,
            "size_changed": (
                obj1.width != obj2.width
                or obj1.height != obj2.height
            ),
            "position_changed": (
                obj1.min_row != obj2.min_row
                or obj1.min_col != obj2.min_col
            ),
            "centroid_changed": (
                obj1.centroid_row != obj2.centroid_row
                or obj1.centroid_col != obj2.centroid_col
            ),
            "pixel_count_changed": len(obj1.pixels) != len(obj2.pixels),
        }