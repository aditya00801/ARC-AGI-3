from src.core.object import ARCObject


class SpatialReasoner:
    """
    Computes spatial relationships between ARC objects.
    """

    @staticmethod
    def manhattan_distance(obj1: ARCObject, obj2: ARCObject) -> float:
        """
        Manhattan distance between object centroids.
        """
        return (
            abs(obj1.centroid_row - obj2.centroid_row)
            + abs(obj1.centroid_col - obj2.centroid_col)
        )

    @staticmethod
    def is_left_of(obj1: ARCObject, obj2: ARCObject) -> bool:
        """
        True if obj1 is left of obj2.
        """
        return obj1.centroid_col < obj2.centroid_col

    @staticmethod
    def is_right_of(obj1: ARCObject, obj2: ARCObject) -> bool:
        """
        True if obj1 is right of obj2.
        """
        return obj1.centroid_col > obj2.centroid_col

    @staticmethod
    def is_above(obj1: ARCObject, obj2: ARCObject) -> bool:
        """
        True if obj1 is above obj2.
        """
        return obj1.centroid_row < obj2.centroid_row

    @staticmethod
    def is_below(obj1: ARCObject, obj2: ARCObject) -> bool:
        """
        True if obj1 is below obj2.
        """
        return obj1.centroid_row > obj2.centroid_row

