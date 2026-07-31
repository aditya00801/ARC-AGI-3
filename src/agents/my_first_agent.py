from typing import Any

from arcengine import FrameData, GameAction, GameState

from agents.agent import Agent

from src.policies.random_policy import RandomPolicy


class MyFirstAgent(Agent):
    """
    Thin adapter between the ARC framework and our policy syatem.
    """

    MAX_ACTIONS = 80 

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args,**kwargs)

        # Attach the decision policy
        self.policy = RandomPolicy()

    @property
    def name(self) -> str:
        return f"{super().name}.policy"

    def is_done(
            self,
            frames: list[FrameData],
            latest_frame : FrameData,
    ) -> bool:
        return latest_frame.state is GameState.WIN

    def chooes_action(
            self,
            frames: list[FrameData],
            latest_frame : FrameData,
    ) -> GameAction:
        return self.policy.decide(frames,latest_frame)

