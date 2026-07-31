# Dataset Structure

```
data/
│
├── environment_files/
│   ├── ar25/
│   ├── bp35/
│   ├── cd82/
│   ├── ...
│
├── ARC-AGI-3-Agents/
│
└── arc_agi_3_wheels/
```

---

## environment_files

Contains public environments.

Each environment consists of

```
environment_name/
    unique_id/
        metadata.json
        game.py
```

Example

```
ar25/
    0c556536/
        ar25.py
        metadata.json
```

---

## ARC-AGI-3-Agents

Official baseline implementation.

To be analyzed in Phase 2.

---

## arc_agi_3_wheels

Offline Python wheel packages required by the competition.