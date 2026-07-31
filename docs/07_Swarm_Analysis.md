# Swarm Analysis

## Purpose

Swarm orchestrates all agents.

It is not responsible for solving puzzles.

---

## Responsibilities

- Open scorecard
- Create one agent per game
- Create environment
- Launch threads
- Wait for completion
- Close scorecard
- Cleanup

---

# Execution

for game in games

↓

Arcade.make()

↓

Create Agent

↓

Thread

↓

Agent.main()

---

# Important Observation

One agent instance is created for every game.