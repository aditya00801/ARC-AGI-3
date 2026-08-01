from src.core.object import ARCObject
from src.learning.rule_validator import RuleValidator


def make_object(
    color: int,
    shape: str = "square",
    area: int = 4,
    width: int = 2,
    height: int = 2,
    row: int = 0,
    col: int = 0,
) -> ARCObject:

    return ARCObject(
        color=color,
        pixels=[],
        area=area,
        min_row=row,
        max_row=row + height - 1,
        min_col=col,
        max_col=col + width - 1,
        width=width,
        height=height,
        centroid_row=row + height / 2,
        centroid_col=col + width / 2,
        shape=shape,
    )


def test_identical_objects():

    predicted = [
        make_object(color=2)
    ]

    expected = [
        make_object(color=2)
    ]

    assert RuleValidator.validate(
        predicted,
        expected,
    )


def test_different_color():

    predicted = [
        make_object(color=2)
    ]

    expected = [
        make_object(color=5)
    ]

    assert not RuleValidator.validate(
        predicted,
        expected,
    )


def test_different_shape():

    predicted = [
        make_object(
            color=2,
            shape="square",
        )
    ]

    expected = [
        make_object(
            color=2,
            shape="line",
        )
    ]

    assert not RuleValidator.validate(
        predicted,
        expected,
    )


def test_different_object_count():

    predicted = [
        make_object(color=2)
    ]

    expected = [
        make_object(color=2),
        make_object(color=3),
    ]

    assert not RuleValidator.validate(
        predicted,
        expected,
    )


def test_empty_lists():

    assert RuleValidator.validate(
        [],
        [],
    )