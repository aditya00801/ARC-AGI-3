from dataclasses import dataclass

@dataclass
class DetectedObject:
    id: int
    color: int

    pixels: list[tuple[int, int]]

    area: int

    width: int
    height: int

    min_row: int
    max_row: int
    min_col: int
    max_col: int

    centroid: tuple[float, float]

    shape: str = "unknown"