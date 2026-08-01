# ARC-AGI-3

An object-centric AI agent for the **ARC Prize 2026 (ARC-AGI-3)** competition.

This project focuses on building an intelligent ARC solver capable of understanding and solving **Abstraction and Reasoning Corpus (ARC)** tasks through modular perception, semantic reasoning, and transformation learning.

---

# Project Objectives

* Study and understand the official ARC-AGI-3 framework.
* Develop a modular custom agent architecture.
* Build an object-centric perception system.
* Construct a semantic World Model.
* Implement an intelligent reasoning engine.
* Develop a transformation engine capable of solving unseen ARC tasks.
* Optimize the agent for the ARC Prize 2026 competition.

---

# Current Status

| Phase                                        | Status     |
| -------------------------------------------- | ---------- |
| Phase 1 – Competition & Environment Analysis | ✅ Complete |
| Phase 2 – Framework Reverse Engineering      | ✅ Complete |
| Phase 3 – Custom Agent Development           | ✅ Complete |
| Phase 4 – Perception System                  | ✅ Complete |
| Phase 5 – Reasoning Engine                   | ✅ Complete |
| Phase 6 – Transformation Engine              | 🚧 Planned |
| Phase 7 – Competition Optimization           | ⏳ Planned  |

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
ARCObject
       │
 ┌─────┴─────────────┐
 ▼                   ▼
ShapeRecognizer  SpatialReasoner
       │
       ▼
PatternDetector
       │
       ▼
ObjectComparator
       │
       ▼
RuleInference
       │
       ▼
DecisionEngine
       │
       ▼
ARCSolver
       │
       ▼
Transformation Engine (Phase 6)
```

---

# Repository Structure

```text
ARC-AGI-3/
│
├── framework/
│   └── ARC-AGI-3-Agents/        # Official ARC-AGI-3 Framework
│
├── docs/                        # Technical Documentation
├── experiments/                 # Experiments and Testing
├── models/                      # Saved Models
├── notebooks/                   # Research Notebooks
├── outputs/                     # Generated Outputs
│
├── src/
│   ├── agents/
│   ├── core/
│   ├── perception/
│   ├── reasoning/
│   ├── policies/
│   └── utils/
│
├── tests/
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Implemented Features

## Agent Framework

* Custom Agent Architecture
* BasePolicy
* RandomPolicy
* MyFirstAgent
* LocalRunner

---

## Perception System

* GridParser
* ColorAnalyzer
* ConnectedComponentExtractor
* WorldBuilder
* WorldModel
* ARCObject

---

## Reasoning Engine

### Object Representation

* ARCObject

### Shape Analysis

* ShapeRecognizer

### Spatial Analysis

* SpatialReasoner

### Pattern Analysis

* PatternDetector

### Object Comparison

* ObjectComparator

### Rule Representation

* Rule

### Rule Learning

* RuleInference

### Decision Making

* DecisionEngine

### Solver Pipeline

* ARCSolver

---

# Documentation

The project contains comprehensive technical documentation in the **docs/** directory.

Documentation includes:

* Competition Analysis
* Framework Architecture
* Agent API
* Policy System
* Agent Development
* Perception Pipeline
* World Model
* Object Model
* Reasoning Engine
* Shape Recognition
* Spatial Reasoning
* Pattern Detection
* Rule Inference
* Decision Engine
* ARC Solver

Documentation currently covers **Phases 1–5**.

---

# Development Roadmap

## ✅ Phase 1 – Competition & Environment Analysis

Completed.

---

## ✅ Phase 2 – Framework Reverse Engineering

Completed.

---

## ✅ Phase 3 – Custom Agent Development

Completed.

---

## ✅ Phase 4 – Perception System

Completed.

Implemented:

* Grid Parser
* Color Analyzer
* Connected Component Extractor
* World Builder
* World Model

---

## ✅ Phase 5 – Reasoning Engine

Completed.

Implemented:

* ARCObject
* ShapeRecognizer
* SpatialReasoner
* PatternDetector
* ObjectComparator
* Rule
* RuleInference
* DecisionEngine
* ARCSolver

---

## 🚧 Phase 6 – Transformation Engine

Planned modules:

* RuleExecutor
* TranslationTransformer
* RotationTransformer
* ReflectionTransformer
* ColorTransformer
* ScalingTransformer
* GridBuilder
* PredictionEngine

---

## ⏳ Phase 7 – Competition Optimization

Planned features:

* Multi-task Evaluation
* Object Matching
* Performance Optimization
* Benchmarking
* Submission Pipeline
* Competition Testing

---

# Current Focus

Development is now focused on **Phase 6 – Transformation Engine**.

The next milestone is to execute the transformation rules inferred by the Reasoning Engine and generate predicted output grids for unseen ARC tasks.

---

# Technologies

* Python 3
* Object-Oriented Programming (OOP)
* Dataclasses
* ARC-AGI-3 Framework
* Git
* GitHub

---

# Version

**Current Version:** `v0.5.0`

**Status:** Phase 5 (Reasoning Engine) Complete

---

# License

This project is developed for research and educational purposes as part of the **ARC Prize 2026 (ARC-AGI-3)** competition.
