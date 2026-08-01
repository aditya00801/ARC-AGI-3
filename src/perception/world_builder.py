from arcengine import FrameData

from src.core.world_model import WorldModel
from src.perception.grid_parser import GridParser
from src.perception.color_analyzer import ColorAnalyzer
from src.perception.connected_components import ConnectedComponentExtractor


class WorldBuilder:
    """
    Builds a complete WorldModel from a FrameData observation.
    """

    @staticmethod
    def build(frame: FrameData) -> WorldModel:

        # Extract grid
        grid = GridParser.extract_grid(frame)

        # Analyze colors
        color_counts = ColorAnalyzer.analyze(grid)

        # Detect objects
        objects = ConnectedComponentExtractor.extract(grid)

        # Background color = most common color
        background_color = max(
            color_counts,
            key=color_counts.get,
        )

        # Largest / smallest object
        largest_object = max(
            objects,
            key=lambda o: o.area,
        )

        smallest_object = min(
            objects,
            key=lambda o: o.area,
        )

        return WorldModel(
            grid=grid,
            objects=objects,
            color_counts=color_counts,
            background_color=background_color,
            largest_object=largest_object,
            smallest_object=smallest_object,
        )