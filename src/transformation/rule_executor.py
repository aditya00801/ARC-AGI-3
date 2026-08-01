from src.reasoning.rule import Rule
from src.core.object import ARCObject


class RuleExecutor:
    """
    Executes transformation rules on ARC objects.
    """

    @staticmethod
    def execute(
        rule: Rule,
        objects: list[ARCObject],
    ) -> list[ARCObject]:
        pass