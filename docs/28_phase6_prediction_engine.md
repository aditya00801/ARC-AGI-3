# PredictionEngine

## Purpose

The **PredictionEngine** is the final component of the Transformation Engine. It generates the predicted output grid by applying the selected transformation rule to the input grid.

It acts as the bridge between the **Reasoning Engine** and the **Transformation Engine**, orchestrating the complete prediction workflow.

---

# API

```python
PredictionEngine.predict(
    input_grid: list[list[int]],
    rule: Rule,
) -> list[list[int]]
```

### Parameters

| Parameter    | Description                                         |
| ------------ | --------------------------------------------------- |
| `input_grid` | Input ARC grid                                      |
| `rule`       | Transformation rule selected by the Decision Engine |

### Returns

```python
list[list[int]]
```

The predicted ARC output grid.

---

# Workflow

```text
Input Grid
      │
      ▼
ConnectedComponentExtractor
      │
      ▼
ARCObject(s)
      │
      ▼
RuleExecutor
      │
      ▼
Selected Transformer
      │
      ▼
Transformed ARCObject(s)
      │
      ▼
GridBuilder
      │
      ▼
Predicted Output Grid
```

Execution steps:

1. Receive the input grid.
2. Extract ARC objects from the grid.
3. Execute the selected transformation rule.
4. Transform the extracted objects.
5. Rebuild the output grid.
6. Return the predicted grid.

---

# Example

## Input Grid

```text
2 2 0
2 0 0
0 0 0
```

## Rule

```python
Rule(
    type="color_change",
    parameters={
        "from": 2,
        "to": 5,
    },
)
```

## Predicted Output

```text
5 5 0
5 0 0
0 0 0
```

---

# Limitations

Current implementation:

* Supports a single transformation rule.
* Assumes the rule has already been inferred correctly.
* Produces an output grid with the same dimensions as the input grid.
* Does not validate the generated prediction against training examples.
* Does not support chained or composite transformations.

---

# Future Work

Planned improvements include:

* Multiple rule execution.
* Sequential transformation pipelines.
* Automatic output grid resizing.
* Object matching between training and test examples.
* Confidence scoring for predictions.
* Validation against training examples before prediction.
* Support for composite transformations (e.g., translation followed by color change).
* Search-based prediction when multiple candidate rules exist.

---

# Integration

The PredictionEngine is the final module of **Phase 6 – Transformation Engine**.

```text
Perception Engine
        │
        ▼
Reasoning Engine
        │
        ▼
DecisionEngine
        │
        ▼
PredictionEngine
        │
        ▼
Predicted Output Grid
```

---

# Module Status

**Phase:** Phase 6 – Transformation Engine

**Status:** ✅ Completed
