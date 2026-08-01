from src.core.object import ARCObject


class RuleValidator:
    """
    Validates transformed objects against expected objects.
    """

    @staticmethod
    def validate(
        predicted_objects: list[ARCObject],
        expected_objects: list[ARCObject],
    ) -> bool:

        if len(predicted_objects) != len(expected_objects):
            return False

        for predicted, expected in zip(
            predicted_objects,
            expected_objects,
        ):

            if predicted.color != expected.color:
                return False

            if predicted.shape != expected.shape:
                return False

            if predicted.area != expected.area:
                return False

            if predicted.width != expected.width:
                return False

            if predicted.height != expected.height:
                return False

            if predicted.min_row != expected.min_row:
                return False

            if predicted.max_row != expected.max_row:
                return False

            if predicted.min_col != expected.min_col:
                return False

            if predicted.max_col != expected.max_col:
                return False

        return True