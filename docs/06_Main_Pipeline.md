# main.py Analysis

## Responsibilities

- Read configuration
- Parse command-line arguments
- Connect to ARC API
- Retrieve available games
- Create Swarm
- Handle logging
- Handle cleanup

---

# Execution Flow

User

↓

main.py

↓

Load .env

↓

GET /api/games

↓

Create Swarm

↓

Run Agent Threads

↓

Close Scorecard

↓

Exit