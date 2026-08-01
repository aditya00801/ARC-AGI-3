from collections import deque

from src.core.object import ARCObject

class ConnectedComponentExtractor:
    """
    Finds connected components (objects) in a grid.
    Uses 4-connectivity (up, down, left, right).
    """

    @staticmethod
    def extract(grid: list[list[int]]) -> list[ARCObject]:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False] * cols for _ in range(rows)]
        objects: list[ARCObject] = []

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]

        for r in range(rows):
            for c in range(cols):

                if visited[r][c]:
                    continue

                color = grid[r][c]

                queue = deque([(r, c)])
                visited[r][c] = True

                pixels = []

                while queue:

                    x, y = queue.popleft()
                    pixels.append((x, y))

                    for dx, dy in directions:

                        nx = x + dx
                        ny = y + dy

                        if (
                            0 <= nx < rows
                            and 0 <= ny < cols
                            and not visited[nx][ny]
                            and grid[nx][ny] == color
                        ):
                            visited[nx][ny] = True
                            queue.append((nx, ny))

                rows_list = [r for r, c in pixels]
                cols_list = [c for r, c in pixels]

                min_row = min(rows_list)
                max_row = max(rows_list)

                min_col = min(cols_list)
                max_col = max(cols_list)

                width = max_col - min_col + 1
                height = max_row - min_row + 1

                centroid_row = sum(rows_list) / len(rows_list)
                centroid_col = sum(cols_list) / len(cols_list)

                objects.append(
                    ARCObject(
                        color=color,
                        pixels=pixels,
                        area=len(pixels),
                        min_row=min_row,
                        max_row=max_row,
                        min_col=min_col,
                        max_col=max_col,
                        width=width,
                        height=height,
                        centroid_row=centroid_row,
                        centroid_col=centroid_col,
                    )
                )

        return objects