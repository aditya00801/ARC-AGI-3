# ARC Engine

Package

arc_agi

---

## Core Classes

Arcade

EnvironmentWrapper

---

# Arcade

Responsibilities

- Scan environments
- Download environments
- Create wrappers
- Manage scorecards
- Serve environments

---

# Arcade.make()

Input

Game ID

Output

EnvironmentWrapper

Supports

- Offline Mode
- Normal Mode
- Online Mode

---

# EnvironmentWrapper

Interface

reset()

step()

observation_space

action_space

info()

Actual implementation is in

- LocalWrapper
- RemoteWrapper