# Connected Component Analysis

## Overview

Connected Component Analysis (CCA) is a core algorithm in the perception system of the ARC-AGI-3 agent.

Its purpose is to identify and separate individual objects within an ARC grid by grouping neighboring cells that share the same color.

Instead of treating the grid as a collection of independent pixels, CCA enables the agent to recognize meaningful objects.

---

# Objectives

The Connected Component Analysis module is responsible for:

- Detecting individual objects.
- Grouping connected cells.
- Separating multiple objects of the same color.
- Providing object data to the World Builder.

---

# Position in the Perception Pipeline

```
Input Grid
     │
     ▼
Grid Parser
     │
     ▼
Color Analyzer
     │
     ▼
Connected Component Analysis
     │
     ▼
World Builder
     │
     ▼
World Model
```

---

# What is a Connected Component?

A connected component is a group of neighboring cells with the same color.

Example:

```
1 1 0 0

1 1 0 2

0 0 2 2

3 0 0 2
```

Detected Objects:

```
Object 1 (Color 1)

■■
■■

Object 2 (Color 2)

 ■
■■
 ■

Object 3 (Color 3)

■
```

Each object is processed independently.

---

# Connectivity

The current implementation uses **4-connectivity**, where each cell is connected to its:

- Up
- Down
- Left
- Right

Diagonal cells are **not** considered connected.

Example:

```
■ □

□ ■
```

These are treated as two separate objects.

---

# Algorithm

The extraction process follows these steps:

1. Scan the grid row by row.
2. Find an unvisited colored cell.
3. Start a search (BFS or DFS).
4. Visit all connected cells of the same color.
5. Mark them as visited.
6. Create a new Object.
7. Continue scanning until the grid is fully processed.

---

# Data Collected

For every connected component:

- Object ID
- Color
- Pixel coordinates
- Area
- Bounding box
- Width
- Height

This information is passed to the World Builder.

---

# Advantages

Connected Component Analysis provides:

- Automatic object detection
- Clear object separation
- Modular processing
- Efficient perception
- Structured input for reasoning

---

# Complexity

For a grid with **N** cells:

- Time Complexity: **O(N)**
- Space Complexity: **O(N)** (visited map and search queue/stack)

Each cell is visited at most once.

---

# Integration

The Connected Component Analysis module receives:

- Parsed grid
- Color information

It outputs:

- List of detected objects

These objects are then converted into semantic entities by the World Builder.

---

# Current Implementation

Implemented:

- 4-connected object detection
- Object extraction
- Pixel grouping
- Integration with World Builder

---

# Future Improvements

Planned enhancements include:

- 8-connectivity (optional)
- Noise filtering
- Hole detection
- Nested object detection
- Shape classification
- Object hierarchy

---

# Summary

Connected Component Analysis is the foundation of object detection in the ARC-AGI-3 perception system. By converting groups of connected cells into structured objects, it enables the World Model and Reasoning Engine to work with meaningful entities instead of raw grid cells.