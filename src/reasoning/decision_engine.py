class DecisionEngine:

    RULE_PRIORITY = {
        "translation": 100,
        "color_change": 90,
        "shape_change": 80,
        "size_change": 70,
    }

    @classmethod
    def choose(cls, rules: list[Rule]) -> Rule | None:

        if not rules:
            return None

        return max(
            rules,
            key=lambda rule: cls.RULE_PRIORITY.get(rule.type, 0)
        )