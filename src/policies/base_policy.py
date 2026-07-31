from abc import ABC, abstractmethod

from arcengine import FrameData, GameAction


class BasePolicy(ABC):
    """
    Base class for every decision policy.
    """

    @abstractmethod
    def decide(
        self,
        frames: list[FrameData],
        latest_frame: FrameData,
    ) -> GameAction:
        """
        Decide the next action.
        """
        raise NotImplementedError