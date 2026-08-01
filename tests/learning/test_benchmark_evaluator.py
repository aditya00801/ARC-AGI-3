from src.core.object import ARCObject
from src.learning.benchmark_evaluator import (
    BenchmarkEvaluator,
)


def make_object(color: int) -> ARCObject:

    return ARCObject(
        color=color,
        pixels=[],
        area=4,
        min_row=0,
        max_row=1,
        min_col=0,
        max_col=1,
        width=2,
        height=2,
        centroid_row=0.5,
        centroid_col=0.5,
        shape="square",
    )


def test_perfect_benchmark():

    predictions = [
        [make_object(2)],
        [make_object(3)],
    ]

    expected = [
        [make_object(2)],
        [make_object(3)],
    ]

    result = BenchmarkEvaluator.evaluate(
        predictions,
        expected,
    )

    assert result.total_tasks == 2
    assert result.solved_tasks == 2
    assert result.accuracy == 1.0
    assert result.average_confidence == 1.0


def test_partial_benchmark():

    predictions = [
        [make_object(2)],
        [make_object(5)],
    ]

    expected = [
        [make_object(2)],
        [make_object(3)],
    ]

    result = BenchmarkEvaluator.evaluate(
        predictions,
        expected,
    )

    assert result.total_tasks == 2
    assert result.solved_tasks == 1
    assert result.accuracy == 0.5


def test_empty_benchmark():

    result = BenchmarkEvaluator.evaluate([], [])

    assert result.total_tasks == 0
    assert result.solved_tasks == 0
    assert result.accuracy == 0.0


def test_invalid_input():

    try:
        BenchmarkEvaluator.evaluate(
            [[make_object(2)]],
            [],
        )
    except ValueError:
        assert True
    else:
        assert False