# Policy System

## Purpose

Policies contain all decision-making logic.

The Agent only delegates decisions.

---

# BasePolicy

BasePolicy defines one interface:

decide(
    frames,
    latest_frame
)

↓

GameAction

---

# Current Policy

RandomPolicy

Responsibilities

- Reset game when necessary.
- Select random actions.
- Generate coordinates for complex actions.
- Return GameAction.

---

# Future Policies

- HeuristicPolicy
- ExplorationPolicy
- PlanningPolicy
- MemoryPolicy
- CompetitionPolicy

All policies inherit from BasePolicy.