from collections import Counter


class ColorAnalyzer:
    """
    Computes statistics about colors in a grid.
    """

    @staticmethod
    def analyze(grid: list[list[int]]) -> dict[int, int]:
        counts = Counter()

        for row in grid:
            counts.update(row)

        return dict(sorted(counts.items()))