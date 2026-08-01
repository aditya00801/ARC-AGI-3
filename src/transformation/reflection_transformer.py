from copy import deepcopy

from src.core.object import ARCObject
from src.reasoning.rule import Rule


class ReflectionTransformer:
    """
    Applies reflection transformations to ARC objects.
    """

    @staticmethod
    def apply(
        rule: Rule,
        objects: list[ARCObject],
    ) -> list[ARCObject]:

        transformed = deepcopy(objects)

        axis = rule.parameters.get("axis", "vertical")

        if axis not in ("vertical", "horizontal"):
            raise NotImplementedError(
                f"Unsupported reflection axis: {axis}"
            )

        for obj in transformed:

            reflected_pixels = []

            for row, col in obj.pixels:

                if axis == "vertical":
                    new_row = row
                    new_col = obj.max_col - (col - obj.min_col)

                else:  # horizontal
                    new_row = obj.max_row - (row - obj.min_row)
                    new_col = col

                reflected_pixels.append((new_row, new_col))

            obj.pixels = reflected_pixels

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