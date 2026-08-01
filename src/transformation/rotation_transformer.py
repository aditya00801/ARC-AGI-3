from copy import deepcopy

from src.core.object import ARCObject
from src.reasoning.rule import Rule


class RotationTransformer:
    """
    Applies rotation transformations to ARC objects.
    """

    @staticmethod
    def apply(
        rule: Rule,
        objects: list[ARCObject],
    ) -> list[ARCObject]:

        transformed = deepcopy(objects)

        angle = rule.parameters.get("angle", 90)

        if angle != 90:
            raise NotImplementedError(
                "Only 90° clockwise rotation is currently supported."
            )

        for obj in transformed:

            width = obj.width
            height = obj.height

            # Convert to local coordinates
            local_pixels = [
                (
                    row - obj.min_row,
                    col - obj.min_col,
                )
                for row, col in obj.pixels
            ]

            # Rotate 90° clockwise
            rotated = [
                (
                    col,
                    height - 1 - row,
                )
                for row, col in local_pixels
            ]

            # Convert back to global coordinates
            obj.pixels = [
                (
                    obj.min_row + row,
                    obj.min_col + col,
                )
                for row, col in rotated
            ]

            rows = [r for r, _ in obj.pixels]
            cols = [c for _, c in obj.pixels]

            obj.min_row = min(rows)
            obj.max_row = max(rows)

            obj.min_col = min(cols)
            obj.max_col = max(cols)

            obj.width = obj.max_col - obj.min_col + 1
            obj.height = obj.max_row - obj.min_row + 1

            obj.centroid_row = sum(rows) / len(rows)
            obj.centroid_col = sum(cols) / len(cols)

        return transformed