from dataclasses import dataclass

from src.core.object import ARCObject


@dataclass
class WorldModel:
    """
    Complete representation of the current game state.
    """

    grid: list[list[int]]

    objects: list[ARCObject]

    color_counts: dict[int, int]

    background_color: int

    largest_object: ARCObject

    smallest_object: ARCObject