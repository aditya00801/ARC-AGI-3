from copy import deepcopy

from src.core.object import ARCObject
from src.reasoning.rule import Rule


class ScalingTransformer:
    """
    Applies scaling transformations to ARC objects.
    """

    @staticmethod
    def apply(
        rule: Rule,
        objects: list[ARCObject],
    ) -> list[ARCObject]:

        transformed = deepcopy(objects)

        factor = rule.parameters.get("factor", 1)

        if factor < 1:
            raise ValueError("Scaling factor must be >= 1")

        for obj in transformed:

            scaled_pixels = []

            for row, col in obj.pixels:

                local_row = row - obj.min_row
                local_col = col - obj.min_col

                for dr in range(factor):
                    for dc in range(factor):

                        scaled_pixels.append(
                            (
                                obj.min_row + local_row * factor + dr,
                                obj.min_col + local_col * factor + dc,
                            )
                        )

            obj.pixels = scaled_pixels

            rows = [r for r, _ in scaled_pixels]
            cols = [c for _, c in scaled_pixels]

            obj.min_row = min(rows)
            obj.max_row = max(rows)

            obj.min_col = min(cols)
            obj.max_col = max(cols)

            obj.width = obj.max_col - obj.min_col + 1
            obj.height = obj.max_row - obj.min_row + 1

            obj.area = len(scaled_pixels)

            obj.centroid_row = sum(rows) / len(rows)
            obj.centroid_col = sum(cols) / len(cols)

        return transformed