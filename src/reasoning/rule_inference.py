from src.core.object import ARCObject
from src.reasoning.object_comparator import ObjectComparator
from src.reasoning.rule import Rule


class RuleInference:
    """
    Infers transformation rules between
    input and output ARC objects.
    """

    @staticmethod
    def infer(
        input_objects: list[ARCObject],
        output_objects: list[ARCObject],
    ) -> list[Rule]:
        """
        Infer transformation rules from corresponding
        input and output objects.

        NOTE:
        Version 1 assumes objects are already matched
        by index (zip). A future ObjectMatcher module
        should replace this assumption.
        """

        rules: list[Rule] = []

        for input_obj, output_obj in zip(input_objects, output_objects):

            comparison = ObjectComparator.compare(
                input_obj,
                output_obj,
            )

            # ----------------------------
            # Color Change
            # ----------------------------
            if comparison["color_changed"]:
                rules.append(
                    Rule(
                        type="color_change",
                        parameters={
                            "from": input_obj.color,
                            "to": output_obj.color,
                        },
                    )
                )

            # ----------------------------
            # Shape Change
            # ----------------------------
            if comparison["shape_changed"]:
                rules.append(
                    Rule(
                        type="shape_change",
                        parameters={
                            "from": input_obj.shape,
                            "to": output_obj.shape,
                        },
                    )
                )

            # ----------------------------
            # Size Change
            # ----------------------------
            if comparison["size_changed"]:
                rules.append(
                    Rule(
                        type="size_change",
                        parameters={
                            "from": {
                                "width": input_obj.width,
                                "height": input_obj.height,
                                "area": input_obj.area,
                            },
                            "to": {
                                "width": output_obj.width,
                                "height": output_obj.height,
                                "area": output_obj.area,
                            },
                        },
                    )
                )

            # ----------------------------
            # Position Change
            # ----------------------------
            if comparison["position_changed"]:

                delta_row = output_obj.min_row - input_obj.min_row
                delta_col = output_obj.min_col - input_obj.min_col

                rules.append(
                    Rule(
                        type="translation",
                        parameters={
                            "from": (
                                input_obj.min_row,
                                input_obj.min_col,
                            ),
                            "to": (
                                output_obj.min_row,
                                output_obj.min_col,
                            ),
                            "delta_row": delta_row,
                            "delta_col": delta_col,
                        },
                    )
                )

        return rules