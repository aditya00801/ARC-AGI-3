import os

print("RandomPolicy loaded from:")
print(os.path.abspath(__file__))

import random

from src.perception.grid_parser import GridParser

from src.perception.color_analyzer import ColorAnalyzer

from src.perception.connected_components import ConnectedComponentExtractor

from src.perception.world_builder import WorldBuilder

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

        print(">>> RandomPolicy.decide() CALLED <<<")


        # Game hasn't started (or ended), so reset it.
        if latest_frame.state in (
            GameState.NOT_PLAYED,
            GameState.GAME_OVER,
        ):
            return GameAction.RESET

        # ======================================================
        # DEBUG: Print observation only once per episode
        # ======================================================
        if len(frames) == 1:

            world = WorldBuilder.build(latest_frame)
            grid = world.grid
            colors = world.color_counts
            objects = world.objects

            print("\nWorld Model")
            print("-" * 40)
            print("Background Color :", world.background_color)
            print("Objects          :", len(world.objects))
            print("Largest Object   :", world.largest_object.area)
            print("Smallest Object  :", world.smallest_object.area)



            print("\n Connected Components")
            print('-' * 30)
            print(f"\nTotal Objects Found : {len(objects)}")

            print("\n largest 10 Objects ")

            largest = sorted(
                objects,
                key=lambda o: o.area,
                reverse=True
            )

            for obj in largest[:10]:
                print(

                    f"Color {obj.color:2d} |"
                    f" Area {obj.area:4d} "
                    f"Size {obj.width}x{obj.height} |"
                    f"Box ({obj.min_row},{obj.min_col}) -> ({obj.max_row},{obj.max_col}) "
                )





            print("\n Color Statistics")
            print('-' * 30) 

            for  color, count in colors.items():
                print(f"Color {color:2d} : {count:4d} cells")


            print("\n" + "=" * 70)
            print("ARC Observation Debug")
            print("=" * 70)

            print(f"Frame Type         : {type(grid)}")
            print(f"Rows               : {len(grid)}")
            print(f"Columns            : {len(grid[0])}")

            print(f"\nGame State         : {latest_frame.state}")
            print(f"Levels Completed   : {latest_frame.levels_completed}")
            print(f"Win Levels         : {latest_frame.win_levels}")
            print(f"Full Reset         : {latest_frame.full_reset}")
            print(f"Game ID            : {latest_frame.game_id}")
            print(f"GUID               : {latest_frame.guid}")

            print("\nAvailable Actions:")
            print(latest_frame.available_actions)

            print("\nTop-left 10×10 Grid:")
            for row in grid[:10]:
                print(row[:10])

            print("=" * 70)

        # ======================================================
        # Select a random non-reset action
        # ======================================================
        action = random.choice(
            [
                a
                for a in GameAction
                if a is not GameAction.RESET
            ]
        )

        # ======================================================
        # Handle simple actions
        # ======================================================
        if action.is_simple():
            action.reasoning = {
                "policy": "RandomPolicy",
                "strategy": "uniform_random_simple",
            }

        # ======================================================
        # Handle complex actions
        # ======================================================
        elif action.is_complex():
            action.set_data(
                {
                    "x": random.randint(0, 63),
                    "y": random.randint(0, 63),
                }
            )

            action.reasoning = {
                "policy": "RandomPolicy",
                "strategy": "uniform_random_complex",
            }

        return action