from src.core.object import ARCObject
from src.reasoning.rule import Rule


class CompositeRuleInference:
    """
    Infers multiple transformation rules.
    """

    @staticmethod
    def infer(
        input_objects: list[ARCObject],
        output_objects: list[ARCObject],
    ) -> list[Rule]:

        rules = []

        if not input_objects or not output_objects:
            return rules

        input_obj = input_objects[0]
        output_obj = output_objects[0]

        # Color change
        if input_obj.color != output_obj.color:
            rules.append(
                Rule(
                    type="color_change",
                    parameters={
                        "from": input_obj.color,
                        "to": output_obj.color,
                    },
                )
            )

        # Translation
        delta_row = (
            output_obj.centroid_row -
            input_obj.centroid_row
        )

        delta_col = (
            output_obj.centroid_col -
            input_obj.centroid_col
        )

        if delta_row != 0 or delta_col != 0:
            rules.append(
                Rule(
                    type="translation",
                    parameters={
                        "delta_row": int(delta_row),
                        "delta_col": int(delta_col),
                    },
                )
            )

        # Shape change placeholder
        if input_obj.shape != output_obj.shape:
            rules.append(
                Rule(
                    type="shape_change",
                    parameters={
                        "from": input_obj.shape,
                        "to": output_obj.shape,
                    },
                )
            )

        return rules