# Object Model

## Overview

The Object Model represents a single connected object detected within an ARC grid.

During the perception stage, every connected component is converted into an Object instance. These objects become the basic entities used by the reasoning engine to understand and solve ARC tasks.

Rather than processing individual cells, the agent reasons about complete objects and their relationships.

---

# Purpose

The Object Model is responsible for:

- Representing a detected object.
- Storing geometric information.
- Recording object properties.
- Providing data for reasoning algorithms.

---

# Position in the Architecture

```
Input Grid

↓

Connected Components

↓

Object

↓

World Model

↓

Reasoning Engine
```

---

# Core Properties

Each Object contains:

| Property | Description |
|----------|-------------|
| ID | Unique object identifier |
| Color | Object color |
| Pixels | List of occupied cells |
| Area | Number of pixels |
| Bounding Box | Smallest enclosing rectangle |
| Width | Bounding box width |
| Height | Bounding box height |

---

# Future Properties

The following properties will be added in later phases:

- Center Point
- Shape Type
- Orientation
- Symmetry
- Perimeter
- Connectivity
- Neighbour Objects
- Distance to Other Objects

---

# Bounding Box

The bounding box stores:

- Minimum Row
- Maximum Row
- Minimum Column
- Maximum Column

Example:

```
Top Left      (2,3)
Bottom Right  (5,7)
```

---

# Area

Area represents the number of pixels belonging to the object.

Example:

```
■■■
■■■

Area = 6
```

---

# Width and Height

Width

```
□□□□□

Width = 5
```

Height

```
□
□
□
□

Height = 4
```

---

# Object Lifecycle

```
Connected Component

↓

Create Object

↓

Compute Properties

↓

Store in World Model

↓

Used by Reasoning Engine
```

---

# Responsibilities

The Object class should:

- Store object information.
- Calculate geometric properties.
- Support future reasoning algorithms.
- Provide a clean interface for querying object data.

---

# Advantages

Using an Object Model provides:

- Better abstraction
- Easier debugging
- Modular architecture
- Reusable code
- Simplified reasoning

---

# Current Implementation

Implemented:

- Object ID
- Color
- Pixel coordinates
- Bounding box
- Width
- Height
- Area

---

# Planned Enhancements

Future versions will include:

- Shape classification
- Rotation information
- Reflection properties
- Spatial relationships
- Pattern descriptors
- Feature vectors

---

# Summary

The Object Model is the fundamental building block of the ARC-AGI-3 perception system. Every detected structure in the grid is represented as an Object, enabling higher-level reasoning based on semantic entities rather than raw pixels.