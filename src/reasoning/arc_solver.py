from src.perception.connected_components import ConnectedComponentExtractor
from src.reasoning.shape_recognizer import ShapeRecognizer
from src.reasoning.rule_inference import RuleInference
from src.reasoning.decision_engine import DecisionEngine


class ARCSolver:
    """
    High-level ARC reasoning pipeline.
    """

    @staticmethod
    def solve(
        input_grid: list[list[int]],
        output_grid: list[list[int]],
    ):
        """
        Learn the transformation rule from one
        input/output training pair.

        Returns
        -------
        Rule | None
        """

        # Extract objects
        input_objects = ConnectedComponentExtractor.extract(input_grid)
        output_objects = ConnectedComponentExtractor.extract(output_grid)

        # Recognize shapes
        ShapeRecognizer.recognize_all(input_objects)
        ShapeRecognizer.recognize_all(output_objects)

        # Infer rules
        rules = RuleInference.infer(
            input_objects,
            output_objects,
        )

        # Select best rule
        best_rule = DecisionEngine.choose(rules)

        return best_rule