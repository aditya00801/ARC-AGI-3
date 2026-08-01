# Phase 5 – Reasoning Engine

## Overview

Phase 5 implements the **Reasoning Engine** for the ARC-AGI-3 project. It builds on the Perception Engine (Phase 4) by interpreting extracted objects, discovering relationships, identifying patterns, inferring transformation rules, and selecting the most appropriate rule for solving ARC tasks.

The goal of this phase is to transform raw object information into semantic knowledge that can later be executed by the Transformation Engine.

---

# Objectives

* Represent extracted objects in a structured format.
* Recognize basic geometric shapes.
* Analyze spatial relationships between objects.
* Detect patterns across multiple objects.
* Compare input and output objects.
* Infer transformation rules.
* Select the best transformation rule.
* Build a complete reasoning pipeline.

---

# Project Structure

```text
src/
├── core/
│   └── object.py
│
├── perception/
│   ├── connected_components.py
│   ├── color_analyzer.py
│   ├── grid_parser.py
│   └── world_builder.py
│
└── reasoning/
    ├── shape_recognizer.py
    ├── spatial_reasoner.py
    ├── pattern_detector.py
    ├── object_comparator.py
    ├── rule.py
    ├── rule_inference.py
    ├── decision_engine.py
    └── arc_solver.py
```

---

# System Architecture

```text
Input Grid
      │
      ▼
ConnectedComponentExtractor
      │
      ▼
ARCObject
      │
 ┌────┴────────────┐
 ▼                 ▼
ShapeRecognizer  SpatialReasoner
      │                 │
      └────────┬────────┘
               ▼
       PatternDetector
               ▼
      ObjectComparator
               ▼
        RuleInference
               ▼
       DecisionEngine
               ▼
          ARCSolver
```

---

# Modules

## 1. ARCObject

Represents a semantic object extracted from the input grid.

### Stored Information

* Color
* Pixels
* Area
* Width
* Height
* Bounding Box
* Centroid
* Shape

Example:

```python
ARCObject(
    color=2,
    pixels=[...],
    area=6,
    width=3,
    height=2,
    centroid_row=4.5,
    centroid_col=6.0,
    shape="rectangle"
)
```

---

## 2. ShapeRecognizer

Identifies the geometric shape of an object.

### Supported Shapes

* Single Pixel
* Horizontal Line
* Vertical Line
* Square
* Rectangle
* Irregular

### Planned Shapes

* L Shape
* T Shape
* Cross
* Hollow Rectangle
* Diagonal
* Composite Shapes

---

## 3. SpatialReasoner

Computes spatial relationships between ARC objects.

### Current Features

* Manhattan Distance
* Left Of
* Right Of
* Above
* Below

### Planned Features

* Touching
* Overlapping
* Containment
* Nearest Object
* Farthest Object
* Horizontal Alignment
* Vertical Alignment

---

## 4. PatternDetector

Analyzes multiple objects and detects shared properties.

### Current Features

* Same Color
* Same Shape
* Same Size

### Planned Features

* Symmetry
* Translation
* Rotation
* Reflection
* Repetition
* Object Count Patterns

---

## 5. ObjectComparator

Compares two ARC objects.

### Current Comparisons

* Color Change
* Shape Change
* Size Change
* Position Change
* Centroid Change
* Pixel Count Change

Purpose:

Provide structured differences for the Rule Inference module.

---

## 6. Rule

Represents an inferred transformation.

Example:

```python
Rule(
    type="color_change",
    parameters={
        "from": 2,
        "to": 5
    }
)
```

---

## 7. RuleInference

Infers transformation rules between training input and output objects.

### Current Rules

* Color Change
* Shape Change
* Size Change
* Translation

### Planned Rules

* Rotation
* Reflection
* Scaling
* Duplication
* Deletion
* Merge
* Split

---

## 8. DecisionEngine

Selects the most appropriate inferred rule.

### Current Implementation

* Returns the highest-priority rule.

### Future Improvements

* Confidence scoring
* Rule ranking
* Multi-rule reasoning
* Conflict resolution

---

## 9. ARCSolver

Coordinates the complete reasoning pipeline.

### Pipeline

1. Extract objects from the input and output grids.
2. Recognize object shapes.
3. Analyze spatial relationships.
4. Detect object-level patterns.
5. Compare corresponding objects.
6. Infer transformation rules.
7. Select the best rule.

---

# Current Pipeline

```text
Input Grid
      │
      ▼
ConnectedComponentExtractor
      │
      ▼
ARCObject
      │
      ▼
ShapeRecognizer
      │
      ▼
SpatialReasoner
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
```

---

# Phase 5 Achievements

* Implemented semantic object representation.
* Added basic shape recognition.
* Implemented spatial reasoning.
* Added pattern detection.
* Built object comparison utilities.
* Created a structured rule representation.
* Implemented rule inference.
* Added a decision engine.
* Built the first complete reasoning pipeline.

---

# Current Limitations

The current implementation can successfully **analyze** ARC training examples and infer candidate transformation rules.

It **does not yet execute** those rules to generate the predicted output grid.

Rule execution is the responsibility of the next phase.

---

# Phase 5 Completion Status

| Component        | Status |
| ---------------- | ------ |
| ARCObject        | ✅      |
| ShapeRecognizer  | ✅      |
| SpatialReasoner  | ✅      |
| PatternDetector  | ✅      |
| ObjectComparator | ✅      |
| Rule             | ✅      |
| RuleInference    | ✅      |
| DecisionEngine   | ✅      |
| ARCSolver        | ✅      |

**Phase 5 Progress:** **100% Complete**

---

# Next Phase

## Phase 6 – Transformation Engine

### Planned Modules

* RuleExecutor
* TranslationTransformer
* RotationTransformer
* ReflectionTransformer
* ColorTransformer
* ScalingTransformer
* GridBuilder
* PredictionEngine

The Transformation Engine will apply the selected transformation rule to unseen test grids and generate the predicted output grid, enabling complete end-to-end ARC task solving.
