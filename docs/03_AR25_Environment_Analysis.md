# AR25 Environment Analysis

## Project

ARC Prize 2026 – ARC-AGI-3

---

# Objective

Reverse engineer one public environment to understand how ARC-AGI-3 environments are implemented before building an AI agent.

---

# Environment

Game ID

AR25

Location

data/environment_files/ar25/0c556536/

Files

- ar25.py
- metadata.json

---

# Metadata

```json
{
    "game_id": "ar25-0c556536",
    "title": "AR25",
    "default_fps": 6,
    "tags": ["keyboard_click"]
}
```

Observations

- Uses keyboard interaction
- Official baseline action sequence provided
- Implemented in Python

---

# Architecture

AR25 inherits from

```
ARCBaseGame
```

Architecture

```
Agent
    │
    ▼
ARC Engine
    │
    ▼
AR25 Environment
```

---

# Main Class

```
class Ar25(ARCBaseGame)
```

---

# Important Methods

| Method | Purpose |
|---------|---------|
| __init__ | Initialize game |
| on_set_level | Load a level |
| step | Execute one action |
| _get_valid_actions | Return legal actions |
| vplrhaovhr | Check win condition |
| dspftbzaav | Update display |

---

# Available Actions

```
available_actions=[1,2,3,4,5,6,7]
```

---

# Action Mapping

| Action | Meaning |
|---------|---------|
| ACTION1 | Move Up |
| ACTION2 | Move Down |
| ACTION3 | Move Left |
| ACTION4 | Move Right |
| ACTION5 | Cycle selected object |
| ACTION6 | Mouse click / coordinate selection |
| ACTION7 | Undo |

---

# State

The environment stores

- Sprite positions
- Selected object
- Undo stack
- Goal objects

---

# Undo

Previous states are stored in

```
self.flqblmrxsla
```

Undo restores a previous state.

---

# Valid Actions

The environment dynamically computes valid actions.

Not every action is legal in every state.

Agents should query valid actions instead of assuming all actions are available.

---

# Win Condition

Solved when every required target location satisfies the environment constraints.

Win checking is performed in

```
vplrhaovhr()
```

---

# Display

Rendering is separate from game logic.

```
dspftbzaav()
```

updates display layers only.

---

# Important Observations

- Game logic is symbolic.
- Environment is sprite based.
- Rendering and logic are separated.
- Dynamic action space.
- Supports undo.
- Uses ARC Engine API.

---

# Conclusion

We now understand

- Environment initialization
- Action space
- Object selection
- Movement
- Undo
- Dynamic valid actions
- Win condition

The next phase is understanding the official agent framework.