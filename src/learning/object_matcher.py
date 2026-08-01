from src.core.object import ARCObject


class ObjectMatcher:
    """
    Matches input objects to output objects using
    a simple similarity scoring algorithm.
    """

    @staticmethod
    def _similarity_score(
        obj1: ARCObject,
        obj2: ARCObject,
    ) -> int:

        score = 0

        if obj1.color == obj2.color:
            score += 3

        if obj1.shape == obj2.shape:
            score += 3

        if obj1.area == obj2.area:
            score += 2

        if obj1.width == obj2.width:
            score += 1

        if obj1.height == obj2.height:
            score += 1

        return score

    @staticmethod
    def match(
        input_objects: list[ARCObject],
        output_objects: list[ARCObject],
    ) -> list[tuple[ARCObject, ARCObject]]:

        if not input_objects or not output_objects:
            return []

        matches = []
        used_outputs = set()

        for input_obj in input_objects:

            best_score = -1
            best_index = None

            for index, output_obj in enumerate(output_objects):

                if index in used_outputs:
                    continue

                score = ObjectMatcher._similarity_score(
                    input_obj,
                    output_obj,
                )

                if score > best_score:
                    best_score = score
                    best_index = index

            if best_index is not None:
                used_outputs.add(best_index)

                matches.append(
                    (
                        input_obj,
                        output_objects[best_index],
                    )
                )

        return matches