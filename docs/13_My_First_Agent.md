# MyFirstAgent

## Purpose

Acts as a bridge between the official ARC framework and our policy system.

---

# Responsibilities

- Receive FrameData.
- Call Policy.decide().
- Return GameAction.

---

# Class Structure

MyFirstAgent

├── MAX_ACTIONS
├── __init__()
├── name
├── is_done()
└── choose_action()

---

# Architecture

ARC Framework

↓

MyFirstAgent

↓

RandomPolicy

---

# Important Observation

The agent contains almost no AI logic.

All intelligence is delegated to the Policy layer.