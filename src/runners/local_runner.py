"""
Local Runner for ARC-AGI-3

Purpose
-------
Provides a standalone offline execution environment for developing,
testing, and debugging custom ARC agents without relying on the
official ARC Prize online launcher.

Responsibilities
----------------
- Initialize the ARC engine
- Discover local environments
- Load a specific environment
- Inspect environment metadata
- Inspect available actions
- Execute custom agents
- Collect debugging information

Future Extensions
-----------------
- Observation inspection
- Agent execution
- Episode loop
- Logging
- Visualization
- Performance metrics
"""

import os
from pathlib import Path
from typing import Optional

from arc_agi import Arcade
from arc_agi.wrapper import EnvironmentWrapper


class LocalRunner:
    """
    Local execution engine for ARC-AGI-3.

    This class replaces the official online launcher during development
    and provides a controlled offline environment for experimenting with
    custom ARC agents.
    """

    def __init__(self):
        """
        Initialize the runner.

        Attributes
        ----------
        arcade
            Main ARC engine controller.

        environment
            Currently loaded environment wrapper.

        agent
            Custom ARC agent (added later).
        """

        self.arcade: Optional[Arcade] = None
        self.environment: Optional[EnvironmentWrapper] = None
        self.agent = None

    # ==========================================================
    # ARC Engine Initialization
    # ==========================================================

    def initialize_arcade(self):
        """
        Initialize the ARC engine in offline mode.

        This configures the required environment variables before
        creating the Arcade controller.
        """

        # Locate the ARC-AGI-3 project root.
        project_root = Path(__file__).resolve().parents[2]

        # Local directory containing downloaded environments.
        environments_dir = project_root / "data" / "environment_files"

        # Force the ARC engine to run completely offline.
        os.environ["OPERATION_MODE"] = "offline"

        # Tell the ARC engine where the environments are stored.
        os.environ["ENVIRONMENTS_DIR"] = str(environments_dir)

        # Create the Arcade controller.
        self.arcade = Arcade()

        print("=" * 60)
        print("ARC Engine Initialized")
        print(f"Mode           : {self.arcade.operation_mode}")
        print(f"Environment Dir: {environments_dir}")
        print("=" * 60)

    # ==========================================================
    # Environment Discovery
    # ==========================================================

    def list_games(self):
        """
        Discover every locally available ARC environment.

        Returns
        -------
        list
            List of EnvironmentInfo objects.
        """

        # Query the Arcade engine.
        games = self.arcade.get_environments()

        print("\nAvailable Games")
        print("=" * 60)

        print(f"Total games found : {len(games)}")

        # Display only the first ten games.
        for game in games[:10]:
            print(f"- {game.game_id}")

        return games

    # ==========================================================
    # Environment Loading
    # ==========================================================

    def load_environment(self, game_id: str):
        """
        Load a local ARC environment.

        Parameters
        ----------
        game_id
            Short environment identifier (e.g. "ar25").

        Stores
        ------
        self.environment
            Loaded EnvironmentWrapper instance.
        """

        print("\nLoading Environment")
        print("=" * 60)
        print(f"Game : {game_id}")

        # Load the environment through the Arcade engine.
        self.environment = self.arcade.make(game_id)

        # Stop if loading failed.
        if self.environment is None:
            print("Failed to load environment.")
            return

        print("Environment loaded successfully.")

        # ------------------------------------------------------
        # Environment Metadata
        # ------------------------------------------------------

        print("\nEnvironment Information")
        print("=" * 60)

        print(self.environment.info)

        # ------------------------------------------------------
        # Action Space
        # ------------------------------------------------------

        print("\nAvailable Actions")
        print("=" * 60)

        actions = self.environment.action_space

        print(f"Total actions: {len(actions)}")

        for action in actions:
            print(action)

        # ------------------------------------------------------
        #  Initial Observation
        # ------------------------------------------------------
        print("\nInitial Observation")
        print("=" * 60)

        observation = self.environment.observation_space
        print(type(observation))
        print(observation)

    # ==========================================================
    # Observation Inspection
    # ==========================================================
    
    def inspect_observation(self):
        """
        Inspect the initial observation returned by the environment.
        """
        if self.environment is None:
            print("Environment not loaded.")
            return

        observation = self.environment.observation_space

        print("\nInitial Observation")
        print("=" * 60 )

        print(f"Type : {type(observation)}")

        print("\nAvailable Attributes")
        print("="*60)

        for attribute in dir(observation):
            if not attribute.startswith("_"):
                print(attribute)

        print("\n Frame Information")
        print("=" * 60)

        if hasattr(observation, "frame"):
            print("Farme found.")
            print(f"Frame type : {type(observation.frame)}")
            print(f"Number of frame arrays : {len(observation.frame)}")
        else:
            print("NO frame attribute found.")


     # ==========================================================
    # Frame Inspection
    # ==========================================================

    def inspect_frame(self):
        """
        Inspect the visual frame returned by the environment.

        This method examines the contents of the `frame` attribute
        inside the initial observation.
        """

        if self.environment is None:
            print("Environment not loaded.")
            return

        observation = self.environment.observation_space
        frame = observation.frame

        print("\nFrame Inspection")
        print("=" * 60)

        print(f"Frame Container Type : {type(frame)}")
        print(f"Frame Count          : {len(frame)}")

        for index, image in enumerate(frame):

            print("\n" + "-" * 60)
            print(f"Frame #{index}")
            print("-" * 60)

            print(f"Object Type : {type(image)}")

            # Print the actual frame object
            print(image)

            # If the frame supports shape (NumPy arrays), print it.
            if hasattr(image, "shape"):
                print(f"Shape : {image.shape}")

            # If the frame supports dtype (NumPy arrays), print it.
            if hasattr(image, "dtype"):
                print(f"Dtype : {image.dtype}")

    # ==========================================================
    # Environment Interaction
    # ==========================================================
    def execute_first_action(self):
     """
     Execute the first available action and inspect the returned observation.

     This verifies that the environment responds correctly to an action
     and allows us to study the transition from one state to the next.
     """

     if self.environment is None:
         print("Environment not loaded.")
         return

     print("\nExecuting First Action")
     print("=" * 60)

     # Get all currently available actions.
     actions = self.environment.action_space

     if not actions:
         print("No actions available.")
         return

     # Select the first available action.
     action = actions[0]

     print(f"Selected Action : {action}")

     # Execute the action.
     next_observation = self.environment.step(action)

     print("\nNext Observation")
     print("=" * 60)

     print(type(next_observation))
     print(next_observation)

     # If the environment returned another FrameDataRaw object,
     # inspect the important fields.
     if next_observation is not None:
 
         print("\nNext State")
         print("=" * 60)

         print(f"State            : {next_observation.state}")
         print(f"Levels Completed : {next_observation.levels_completed}")
         print(f"Win Levels       : {next_observation.win_levels}")
         print(f"Available Actions: {next_observation.available_actions}")

         if hasattr(next_observation, "frame"):
             print(f"Frame Count      : {len(next_observation.frame)}")



    # ==========================================================
    # Agent Creation
    # ==========================================================

    def create_agent(self):
        """
        Create the custom ARC agent.

        This will be implemented in Phase 3.
        """
        pass

    # ==========================================================
    # Runner
    # ==========================================================

    def run(self):
        """
        Execute the local development pipeline.
        """

        self.initialize_arcade()

        self.list_games()

        self.load_environment("ar25")

        self.inspect_observation()

        self.inspect_frame()

        self.execute_first_action()

    # ==========================================================
    # Summary
    # ==========================================================

    def print_summary(self):
        """
        Display execution statistics.

        Will be expanded in future phases.
        """
        pass


# ==============================================================
# Entry Point
# ==============================================================

if __name__ == "__main__":
    runner = LocalRunner()
    runner.run()