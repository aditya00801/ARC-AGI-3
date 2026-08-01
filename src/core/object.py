from dataclasses import dataclass


@dataclass
class ARCObject:

    color: int

    pixels: list[tuple[int, int]]

    area: int

    min_row: int
    max_row: int

    min_col: int
    max_col: int

    width: int
    height: int

    centroid_row: float
    centroid_col: float