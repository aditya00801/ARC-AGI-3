from src.core.object import ARCObject


class GridBuilder:
    """
    Builds an ARC grid from ARC objects.
    """

    @staticmethod
    def build(
        objects: list[ARCObject],
        rows: int,
        cols: int,
        background_color: int = 0,
    ) -> list[list[int]]:

        grid = [
            [background_color for _ in range(cols)]
            for _ in range(rows)
        ]

        for obj in objects:
            for row, col in obj.pixels:

                if 0 <= row < rows and 0 <= col < cols:
                    grid[row][col] = obj.color

        return grid