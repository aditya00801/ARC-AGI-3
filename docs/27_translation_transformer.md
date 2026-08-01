# TranslationTransformer

## Overview

The **TranslationTransformer** is responsible for moving ARC objects from one position to another based on a translation rule inferred by the Reasoning Engine.

It is the first transformer capable of modifying the spatial location of objects while preserving their semantic properties.

---

# Purpose

The TranslationTransformer applies **translation** transformations to one or more `ARCObject` instances.

A translation changes the position of an object without changing its:

* Color
* Shape
* Area
* Width
* Height

Only the object's location is updated.

---

# Responsibilities

The transformer performs the following operations:

* Translate every pixel of the object.
* Update the bounding box.
* Update the centroid.
* Preserve all non-spatial properties.

---

# Input

## Rule

```python
Rule(
    type="translation",
    parameters={
        "delta_row": 2,
        "delta_col": -1,
    },
)
```

## Objects

```python
list[ARCObject]
```

---

# Output

```python
list[ARCObject]
```

A new list of translated objects is returned while the original objects remain unchanged.

---

# Public API

```python
TranslationTransformer.apply(
    rule,
    objects,
)
```

### Parameters

| Name    | Description              |
| ------- | ------------------------ |
| rule    | Translation rule         |
| objects | ARC objects to translate |

### Returns

A new list of translated `ARCObject` instances.

---

# Transformation Workflow

```text
Rule
      │
      ▼
TranslationTransformer
      │
      ▼
Move Pixels
      │
      ▼
Update Bounding Box
      │
      ▼
Update Centroid
      │
      ▼
Return New Objects
```

---

# Updated Properties

The following properties are modified:

* pixels
* min_row
* max_row
* min_col
* max_col
* centroid_row
* centroid_col

---

# Preserved Properties

The following properties remain unchanged:

* color
* area
* width
* height
* shape

---

# Example

## Before

```text
Pixels

(2,3)
(2,4)
(3,3)
```

Translation Rule

```text
Δrow = +2
Δcol = -1
```

## After

```text
Pixels

(4,2)
(4,3)
(5,2)
```

---

# Current Limitations

Current implementation:

* Applies the translation to every object provided.
* Assumes a valid translation rule.
* Does not check grid boundaries.
* Does not detect collisions between translated objects.
* Does not support object-specific translation.

---

# Future Improvements

Planned enhancements include:

* Translate selected objects only.
* Boundary validation.
* Collision detection.
* Object matching before translation.
* Support multiple translation rules.
* Translation history for debugging.

---

# Integration

The TranslationTransformer is part of the Phase 6 Transformation Engine.

```text
RuleInference
      │
      ▼
DecisionEngine
      │
      ▼
RuleExecutor
      │
      ▼
TranslationTransformer
      │
      ▼
Translated ARCObjects
```

---

# Phase

**Phase 6 – Transformation Engine**

**Module Status:** ✅ Completed
