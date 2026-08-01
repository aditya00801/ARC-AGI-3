from copy import deepcopy

from src.core.object import ARCObject
from src.reasoning.rule import Rule


class TranslationTransformer:
    """
    Applies translation rules to ARC objects.
    """

    @staticmethod
    def apply(
        rule: Rule,
        objects: list[ARCObject],
    ) -> list[ARCObject]:

        transformed = deepcopy(objects)

        delta_row = rule.parameters["delta_row"]
        delta_col = rule.parameters["delta_col"]

        for obj in transformed:

            # Move every pixel
            obj.pixels = [
                (row + delta_row, col + delta_col)
                for row, col in obj.pixels
            ]

            # Update bounding box
            obj.min_row += delta_row
            obj.max_row += delta_row

            obj.min_col += delta_col
            obj.max_col += delta_col

            # Update centroid
            obj.centroid_row += delta_row
            obj.centroid_col += delta_col

        return transformed