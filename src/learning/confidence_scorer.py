from src.core.object import ARCObject


class ConfidenceScorer:
    """
    Computes a confidence score between predicted
    and expected objects.
    """

    @staticmethod
    def score(
        predicted_objects: list[ARCObject],
        expected_objects: list[ARCObject],
    ) -> float:

        if len(predicted_objects) != len(expected_objects):
            return 0.0

        total = 0
        matched = 0

        for predicted, expected in zip(
            predicted_objects,
            expected_objects,
        ):

            comparisons = [
                predicted.color == expected.color,
                predicted.shape == expected.shape,
                predicted.area == expected.area,
                predicted.width == expected.width,
                predicted.height == expected.height,
                predicted.min_row == expected.min_row,
                predicted.max_row == expected.max_row,
                predicted.min_col == expected.min_col,
                predicted.max_col == expected.max_col,
            ]

            total += len(comparisons)
            matched += sum(comparisons)

        if total == 0:
            return 1.0

        return matched / total