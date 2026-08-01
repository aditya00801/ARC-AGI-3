from arcengine import FrameData


class GridParser:
    """
    Extract the playable grid from ARC FrameData.
    """

    @staticmethod
    def extract_grid(frame: FrameData) -> list[list[int]]:
        """
        Returns the 64x64 integer grid.
        """

        if len(frame.frame) == 1:
            return frame.frame[0]

        return frame.frame