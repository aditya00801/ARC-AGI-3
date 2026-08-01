# ARC-AGI-3

An object-centric AI agent for the **ARC Prize 2026 (ARC-AGI-3)** competition.

This project focuses on building an intelligent ARC solver capable of understanding and solving Abstract Reasoning Corpus (ARC) tasks through modular perception, world modeling, and reasoning.

---

# Project Objectives

- Study and understand the official ARC-AGI-3 framework.
- Develop a modular custom agent architecture.
- Build an object-centric perception system.
- Construct a semantic World Model.
- Implement an intelligent reasoning engine.
- Optimize the agent for the ARC Prize 2026 competition.

---

# Current Status

| Phase | Status |
|--------|--------|
| Phase 1 – Competition & Environment Analysis | ✅ Complete |
| Phase 2 – Framework Reverse Engineering | ✅ Complete |
| Phase 3 – Custom Agent Development | ✅ Complete |
| Phase 4 – Perception System | ✅ Complete |
| Phase 5 – Reasoning Engine | 🚧 In Progress |
| Phase 6 – Competition Optimization | ⏳ Planned |

---

# Project Architecture

```text
ARC Environment
       │
       ▼
Input Grid
       │
       ▼
GridParser
       │
       ▼
ColorAnalyzer
       │
       ▼
ConnectedComponentExtractor
       │
       ▼
WorldBuilder
       │
       ▼
WorldModel
       │
       ▼
Reasoning Engine
       │
       ▼
Policy
       │
       ▼
Action
```

---

# Repository Structure

```text
ARC-AGI-3/
│
├── framework/
│   └── ARC-AGI-3-Agents/      # Official ARC-AGI-3 Framework
│
├── docs/                      # Technical Documentation
├── experiments/               # Experiments and Testing
├── models/                    # Saved Models
├── notebooks/                 # Research Notebooks
├── outputs/                   # Generated Outputs
│
├── src/
│   ├── agents/
│   ├── core/
│   ├── perception/
│   ├── policies/
│   └── ...
│
├── tests/
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Implemented Features

## Agent Framework

- Custom Agent Architecture
- BasePolicy
- RandomPolicy
- MyFirstAgent
- LocalRunner

---

## Perception System

- GridParser
- ColorAnalyzer
- ConnectedComponentExtractor
- WorldBuilder
- WorldModel
- Object

---

## Documentation

Complete documentation for:

- Phase 1 – Competition & Environment Analysis
- Phase 2 – Framework Reverse Engineering
- Phase 3 – Custom Agent Development
- Phase 4 – Perception System

---

# Documentation

The project contains comprehensive technical documentation located in the **docs/** directory.

Documentation includes:

- Competition Analysis
- Framework Architecture
- ARC Engine
- Agent API
- Policy System
- Agent Development
- Grid Parser
- Color Analysis
- Connected Component Analysis
- World Builder
- World Model
- Object Model
- Perception Pipeline

A total of **25 technical documents** currently describe the complete development process through Phase 4.

---

# Roadmap

## Phase 5 – Reasoning Engine

Planned features:

- Object Property Extraction
- Spatial Relationship Analysis
- Shape Recognition
- Pattern Detection
- Rule Inference
- Intelligent Decision Making
- ARC Task Solving

---

## Phase 6 – Competition Optimization

Planned features:

- Multi-task Evaluation
- Performance Optimization
- Benchmarking
- Submission Pipeline
- Competition Testing

---

# Current Focus

Development is now focused on **Phase 5 – Reasoning Engine**.

The next milestone is to transform the structured **WorldModel** produced by the perception system into an intelligent reasoning system capable of discovering transformation rules and solving unseen ARC tasks.

---

# Technologies

- Python 3
- Object-Oriented Programming
- ARC-AGI-3 Framework
- Git
- GitHub

---

# License

This project is developed for research and educational purposes as part of the **ARC Prize 2026 (ARC-AGI-3)** competition.