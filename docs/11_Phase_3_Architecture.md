# Phase 3 - Custom Agent Architecture

## Objective

Build a modular ARC-AGI-3 agent while keeping the official framework untouched.

---

# Architecture Philosophy

Official Framework

↓

Framework Adapter

↓

Policy

↓

AI Components

---

# Directory Structure

src/

├── agents/
├── policies/
├── memory/
├── perception/
├── planning/
├── core/
├── utils/
└── config/

---

# Design Principles

- Keep the official framework read-only.
- Store all custom code in src/.
- Separate framework integration from AI logic.
- Make every component independently replaceable.

---

# Data Flow

Environment

↓

FrameData

↓

MyFirstAgent

↓

Policy

↓

GameAction

↓

Environment