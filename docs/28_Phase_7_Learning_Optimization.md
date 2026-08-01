# Phase 7 – Learning & Optimization

## Overview

Phase 7 focuses on improving the intelligence and generalization capability of the ARC solver.

The previous phases established the complete pipeline:

* Perception Engine
* Reasoning Engine
* Transformation Engine

This phase enhances the solver by introducing learning-based components that improve object correspondence, rule inference, prediction accuracy, and evaluation.

---

# Objectives

* Learn relationships between input and output objects.
* Improve transformation rule inference.
* Support multiple transformation rules.
* Validate inferred rules.
* Rank candidate solutions.
* Benchmark solver performance.

---

# Architecture

```text
Training Examples
        │
        ▼
ObjectMatcher
        │
        ▼
Rule Inference
        │
        ▼
Rule Validation
        │
        ▼
Confidence Scoring
        │
        ▼
Prediction Engine
```

---

# Step 1 – ObjectMatcher

## Purpose

The ObjectMatcher determines which input object corresponds to which output object in ARC training examples.

Object correspondence is essential before transformation rules can be inferred correctly.

---

## Responsibilities

* Compare every input object with every output object.
* Compute similarity scores.
* Select the best matching object.
* Return matched object pairs.

---

## Similarity Features

Version 1 compares objects using:

* Color
* Shape
* Area
* Width
* Height

Each matching property contributes to an overall similarity score.

---

## Matching Algorithm

The current implementation uses a greedy matching strategy:

1. Compare an input object with every unused output object.
2. Compute a similarity score.
3. Select the highest-scoring output object.
4. Repeat until all input objects are processed.

---

## API

```python
ObjectMatcher.match(
    input_objects,
    output_objects,
)
```

Returns:

```python
list[tuple[ARCObject, ARCObject]]
```

---

## Example

Input Objects

```text
Square (Red)

Line (Blue)
```

Output Objects

```text
Line (Blue)

Square (Red)
```

Result

```text
Square (Red)
        │
        ▼
Square (Red)

Line (Blue)
        │
        ▼
Line (Blue)
```

---

## Testing

Unit tests have been implemented for:

* Single object matching.
* Multiple object matching.
* Empty input/output lists.

Current test result:

```text
3 tests passed
```

---

## Current Limitations

Version 1:

* Greedy matching.
* One-to-one correspondence.
* Fixed similarity weights.
* No confidence score.
* No optimal assignment algorithm.

---

## Future Improvements

Planned enhancements include:

* Hungarian assignment algorithm.
* Confidence scoring.
* Learned similarity metrics.
* Spatial relationship matching.
* Multi-object correspondence.
* Robust handling of ambiguous matches.

---

## Phase 7 Progress

| Step                              | Status     |
| --------------------------------- | ---------- |
| Step 1 – ObjectMatcher            | ✅ Complete |
| Step 2 – Composite Rule Inference | ⏳ Planned  |
| Step 3 – Multi-Rule Execution     | ⏳ Planned  |
| Step 4 – Rule Validation          | ⏳ Planned  |
| Step 5 – Confidence Scoring       | ⏳ Planned  |
| Step 6 – Benchmark Evaluation     | ⏳ Planned  |
