import random

from arcengine import FrameData, GameAction, GameState

from .base_policy import BasePolicy


class RandomPolicy(BasePolicy):
    """
    Simple baseline policy that chooses actions randomly.
    """

    def decide(
        self,
        frames: list[FrameData],
        latest_frame: FrameData,
    ) -> GameAction:

        # Game hasn't started (or ended), so reset it.
        if latest_frame.state in (
            GameState.NOT_PLAYED,
            GameState.GAME_OVER,
        ):
            return GameAction.RESET

        # Select a random non-reset action.
        action = random.choice(
            [
                a
                for a in GameAction
                if a is not GameAction.RESET
            ]
        )

        # Handle simple actions.
        if action.is_simple():
            action.reasoning = "RandomPolicy"

        # Handle actions that require coordinates.
        elif action.is_complex():
            action.set_data(
                {
                    "x": random.randint(0, 63),
                    "y": random.randint(0, 63),
                }
            )
            action.reasoning = {
                "policy": "RandomPolicy",
                "strategy": "uniform_random",
            }

        return action