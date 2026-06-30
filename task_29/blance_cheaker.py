class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def is_balanced(expr):
    """
    Returns True if all brackets in expr are balanced.
    Handles: () [] {} and ignores other characters.
    """
    stack = Stack()

    opening = set("({[")
    match = {")": "(", "}": "{", "]": "["}

    for ch in expr:
        if ch in opening:
            stack.push(ch)

        elif ch in match:
            if stack.is_empty():
                return False

            top = stack.pop()

            if top != match[ch]:
                return False

    return stack.is_empty()


# ---- Comprehensive Test Cases ----
test_cases = [
    ("({[]})", True, "Correctly nested"),
    ("()[]{}", True, "Sequential — all correct"),
    ("([)]", False, "Wrong close order"),
    ("((((", False, "Only opens, no close"),
    ("}}}}", False, "Only closes, no open"),
    ("{[()]}", True, "Triple nested"),
    ("", True, "Empty string"),
    ("a+(b*c)", True, "Embedded in expression"),
    ("{[(])}", False, "Interleaved wrong order"),
]

# Print Header
print(f"{'Expression':<16} {'Expected':<10} {'Got':<10} Status")
print("-" * 60)

# Run Test Cases
for expr, expected, desc in test_cases:
    result = is_balanced(expr)
    status = "PASS" if result == expected else "FAIL"

    print(f"{expr!r:<16} {str(expected):<10} {str(result):<10} [{status}] {desc}")