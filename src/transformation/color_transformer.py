from copy import deepcopy

from src.core.object import ARCObject
from src.reasoning.rule import Rule


class ColorTransformer:
    """
    Applies color transformation rules.
    """

    @staticmethod
    def apply(
        rule: Rule,
        objects: list[ARCObject],
    ) -> list[ARCObject]:

        transformed = deepcopy(objects)

        old_color = rule.parameters["from"]
        new_color = rule.parameters["to"]

        for obj in transformed:
            if obj.color == old_color:
                obj.color = new_color

        return transformed