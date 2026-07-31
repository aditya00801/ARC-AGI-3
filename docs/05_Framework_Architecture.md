# Phase 2 - Framework Architecture

## Objective

Understand the official ARC-AGI-3 framework before implementing a custom agent.

---

# High-Level Architecture

                User
                  │
                  ▼
            python main.py
                  │
                  ▼
               Swarm
                  │
                  ▼
               Agent
                  │
                  ▼
        EnvironmentWrapper
                  │
                  ▼
               Arcade
                  │
      ┌───────────┴───────────┐
      │                       │
Local Wrapper         Remote Wrapper
      │                       │
      ▼                       ▼
Environment Files        ARC API Server

---

# Layers

Layer 1

Competition Entry

main.py

Layer 2

Execution

Swarm

Layer 3

Decision Making

Agent

Layer 4

Environment Interface

EnvironmentWrapper

Layer 5

Environment Manager

Arcade

Layer 6

Actual Games

ar25.py
bp35.py
...

---

# Key Design Patterns

- Factory Pattern
- Abstract Base Class
- Wrapper Pattern
- Strategy Pattern
- Thread-based Parallelism