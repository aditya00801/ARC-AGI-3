from src.core.object import ARCObject
from src.learning.object_matcher import ObjectMatcher


def make_object(
    color: int,
    area: int,
    width: int,
    height: int,
    shape: str,
) -> ARCObject:
    return ARCObject(
        color=color,
        pixels=[],
        area=area,
        min_row=0,
        max_row=height - 1,
        min_col=0,
        max_col=width - 1,
        width=width,
        height=height,
        centroid_row=0.0,
        centroid_col=0.0,
        shape=shape,
    )


def test_single_object_match():

    input_objects = [
        make_object(
            color=2,
            area=4,
            width=2,
            height=2,
            shape="square",
        )
    ]

    output_objects = [
        make_object(
            color=2,
            area=4,
            width=2,
            height=2,
            shape="square",
        )
    ]

    matches = ObjectMatcher.match(
        input_objects,
        output_objects,
    )

    assert len(matches) == 1
    assert matches[0][0] == input_objects[0]
    assert matches[0][1] == output_objects[0]


def test_multiple_object_match():

    input_objects = [
        make_object(2, 4, 2, 2, "square"),
        make_object(3, 3, 3, 1, "line"),
    ]

    output_objects = [
        make_object(3, 3, 3, 1, "line"),
        make_object(2, 4, 2, 2, "square"),
    ]

    matches = ObjectMatcher.match(
        input_objects,
        output_objects,
    )

    assert len(matches) == 2

    assert matches[0][1].shape == "square"
    assert matches[1][1].shape == "line"


def test_empty_lists():

    matches = ObjectMatcher.match([], [])

    assert matches == []