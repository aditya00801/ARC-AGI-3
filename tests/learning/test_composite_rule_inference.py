from src.core.object import ARCObject
from src.learning.composite_rule_inference import CompositeRuleInference


def make_object(
    color: int,
    shape: str,
    centroid_row: float,
    centroid_col: float,
) -> ARCObject:
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
        centroid_row=centroid_row,
        centroid_col=centroid_col,
        shape=shape,
    )


def test_no_transformation():

    input_objects = [
        make_object(
            color=2,
            shape="square",
            centroid_row=5,
            centroid_col=5,
        )
    ]

    output_objects = [
        make_object(
            color=2,
            shape="square",
            centroid_row=5,
            centroid_col=5,
        )
    ]

    rules = CompositeRuleInference.infer(
        input_objects,
        output_objects,
    )

    assert rules == []


def test_color_change():

    input_objects = [
        make_object(2, "square", 5, 5)
    ]

    output_objects = [
        make_object(5, "square", 5, 5)
    ]

    rules = CompositeRuleInference.infer(
        input_objects,
        output_objects,
    )

    assert len(rules) == 1
    assert rules[0].type == "color_change"


def test_translation():

    input_objects = [
        make_object(2, "square", 2, 3)
    ]

    output_objects = [
        make_object(2, "square", 6, 8)
    ]

    rules = CompositeRuleInference.infer(
        input_objects,
        output_objects,
    )

    assert len(rules) == 1
    assert rules[0].type == "translation"


def test_color_and_translation():

    input_objects = [
        make_object(2, "square", 1, 1)
    ]

    output_objects = [
        make_object(4, "square", 4, 5)
    ]

    rules = CompositeRuleInference.infer(
        input_objects,
        output_objects,
    )

    assert len(rules) == 2

    assert rules[0].type == "color_change"
    assert rules[1].type == "translation"


def test_shape_change():

    input_objects = [
        make_object(2, "square", 2, 2)
    ]

    output_objects = [
        make_object(2, "line", 2, 2)
    ]

    rules = CompositeRuleInference.infer(
        input_objects,
        output_objects,
    )

    assert len(rules) == 1
    assert rules[0].type == "shape_change"


def test_empty_input():

    rules = CompositeRuleInference.infer([], [])

    assert rules == []