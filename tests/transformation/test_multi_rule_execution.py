from src.core.object import ARCObject
from src.reasoning.rule import Rule
from src.transformation.rule_executor import RuleExecutor


def make_object(
    color: int,
    row: int = 0,
    col: int = 0,
) -> ARCObject:

    return ARCObject(
        color=color,
        pixels=[(row, col)],
        area=1,
        min_row=row,
        max_row=row,
        min_col=col,
        max_col=col,
        width=1,
        height=1,
        centroid_row=float(row),
        centroid_col=float(col),
        shape="pixel",
    )


def test_color_then_translation():

    obj = make_object(color=2)

    rules = [
        Rule(
            type="color_change",
            parameters={
                "from": 2,
                "to": 5,
            },
        ),
        Rule(
            type="translation",
            parameters={
                "delta_row": 2,
                "delta_col": 3,
            },
        ),
    ]

    result = RuleExecutor.execute(rules, [obj])

    assert result[0].color == 5
    assert result[0].pixels == [(2, 3)]


def test_translation_then_reflection():

    obj = make_object(color=4)

    rules = [
        Rule(
            type="translation",
            parameters={
                "delta_row": 1,
                "delta_col": 1,
            },
        ),
        Rule(
            type="reflection",
            parameters={
                "axis": "horizontal",
            },
        ),
    ]

    result = RuleExecutor.execute(rules, [obj])

    assert len(result) == 1


def test_multiple_rules():

    obj = make_object(color=3)

    rules = [
        Rule(
            type="color_change",
            parameters={
                "from": 3,
                "to": 7,
            },
        ),
        Rule(
            type="translation",
            parameters={
                "delta_row": 1,
                "delta_col": 2,
            },
        ),
        Rule(
            type="rotation",
            parameters={
                "angle": 90,
            },
        ),
    ]

    result = RuleExecutor.execute(rules, [obj])

    assert result[0].color == 7


def test_empty_rule_list():

    obj = make_object(color=9)

    result = RuleExecutor.execute([], [obj])

    assert result[0].color == 9
    assert result[0].pixels == [(0, 0)]