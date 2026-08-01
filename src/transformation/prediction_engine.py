from src.perception.connected_components import ConnectedComponentExtractor
from src.transformation.rule_executor import RuleExecutor
from src.transformation.grid_builder import GridBuilder
from src.reasoning.rule import Rule


class PredictionEngine:
    """
    Generates a predicted ARC output grid.
    """

    @staticmethod
    def predict(
        input_grid: list[list[int]],
        rule: Rule,
    ) -> list[list[int]]:

        # Extract objects
        objects = ConnectedComponentExtractor.extract(input_grid)

        # Execute transformation
        transformed_objects = RuleExecutor.execute(
            rule,
            objects,
        )

        # Build output grid
        rows = len(input_grid)
        cols = len(input_grid[0])

        return GridBuilder.build(
            transformed_objects,
            rows,
            cols,
        )