from src.core.object import ARCObject
from src.learning.confidence_scorer import ConfidenceScorer


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


def test_perfect_match():

    predicted = [
        make_object(color=2)
    ]

    expected = [
        make_object(color=2)
    ]

    score = ConfidenceScorer.score(
        predicted,
        expected,
    )

    assert score == 1.0


def test_different_color():

    predicted = [
        make_object(color=2)
    ]

    expected = [
        make_object(color=5)
    ]

    score = ConfidenceScorer.score(
        predicted,
        expected,
    )

    assert score < 1.0
    assert score > 0.0


def test_different_object_count():

    predicted = [
        make_object(color=2)
    ]

    expected = [
        make_object(color=2),
        make_object(color=3),
    ]

    score = ConfidenceScorer.score(
        predicted,
        expected,
    )

    assert score == 0.0


def test_empty_lists():

    score = ConfidenceScorer.score(
        [],
        [],
    )

    assert score == 1.0


def test_multiple_objects():

    predicted = [
        make_object(color=2),
        make_object(color=3),
    ]

    expected = [
        make_object(color=2),
        make_object(color=3),
    ]

    score = ConfidenceScorer.score(
        predicted,
        expected,
    )

    assert score == 1.0