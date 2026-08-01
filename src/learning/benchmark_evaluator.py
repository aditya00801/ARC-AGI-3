from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter

from src.core.object import ARCObject
from src.learning.confidence_scorer import ConfidenceScorer
from src.learning.rule_validator import RuleValidator


@dataclass
class BenchmarkResult:
    """
    Stores benchmark statistics for the ARC solver.
    """

    total_tasks: int
    solved_tasks: int
    accuracy: float
    average_confidence: float
    average_runtime_ms: float


class BenchmarkEvaluator:
    """
    Evaluates solver performance on a collection
    of ARC tasks.
    """

    @staticmethod
    def evaluate(
        predictions: list[list[ARCObject]],
        expected_outputs: list[list[ARCObject]],
    ) -> BenchmarkResult:

        if len(predictions) != len(expected_outputs):
            raise ValueError(
                "Prediction and expected output counts do not match."
            )

        total_tasks = len(predictions)

        if total_tasks == 0:
            return BenchmarkResult(
                total_tasks=0,
                solved_tasks=0,
                accuracy=0.0,
                average_confidence=0.0,
                average_runtime_ms=0.0,
            )

        solved_tasks = 0
        confidence_sum = 0.0
        runtime_sum = 0.0

        for predicted, expected in zip(
            predictions,
            expected_outputs,
        ):

            start = perf_counter()

            valid = RuleValidator.validate(
                predicted,
                expected,
            )

            confidence = ConfidenceScorer.score(
                predicted,
                expected,
            )

            runtime = (
                perf_counter() - start
            ) * 1000.0

            if valid:
                solved_tasks += 1

            confidence_sum += confidence
            runtime_sum += runtime

        return BenchmarkResult(
            total_tasks=total_tasks,
            solved_tasks=solved_tasks,
            accuracy=solved_tasks / total_tasks,
            average_confidence=confidence_sum / total_tasks,
            average_runtime_ms=runtime_sum / total_tasks,
        )