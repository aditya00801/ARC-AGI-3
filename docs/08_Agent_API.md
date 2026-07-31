# Agent API

Agent inherits from ABC.

The framework controls execution.

The user implements only two methods.

---

## Required Methods

choose_action()

Returns GameAction.

This is the intelligence of the system.

---

is_done()

Returns whether execution should stop.

---

# Agent Loop

while not done

↓

Observe

↓

choose_action()

↓

take_action()

↓

Environment.step()

↓

Receive Frame

↓

Repeat

---

# Observation

FrameData

Contains

- frame
- state
- available_actions
- levels_completed
- guid