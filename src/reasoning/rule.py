from dataclasses import dataclass, field


@dataclass(slots=True)
class Rule:
    """
    Represents an inferred transformation rule.
    """

    type: str
    parameters: dict = field(default_factory=dict)