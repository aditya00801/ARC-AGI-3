from src.core.object import ARCObject
from src.reasoning.rule import Rule

from src.transformation.color_transformer import ColorTransformer
from src.transformation.translation_transformer import TranslationTransformer
from src.transformation.rotation_transformer import RotationTransformer
from src.transformation.reflection_transformer import ReflectionTransformer
from src.transformation.scaling_transformer import ScalingTransformer


class RuleExecutor:
    """
    Executes an ordered sequence of transformation rules.
    """

    @staticmethod
    def execute(
        rules: list[Rule],
        objects: list[ARCObject],
    ) -> list[ARCObject]:

        transformed = objects

        for rule in rules:

            if rule.type == "color_change":
                transformed = ColorTransformer.apply(
                    rule,
                    transformed,
                )

            elif rule.type == "translation":
                transformed = TranslationTransformer.apply(
                    rule,
                    transformed,
                )

            elif rule.type == "rotation":
                transformed = RotationTransformer.apply(
                    rule,
                    transformed,
                )

            elif rule.type == "reflection":
                transformed = ReflectionTransformer.apply(
                    rule,
                    transformed,
                )

            elif rule.type == "scaling":
                transformed = ScalingTransformer.apply(
                    rule,
                    transformed,
                )

            else:
                raise ValueError(
                    f"Unsupported rule type: {rule.type}"
                )

        return transformed