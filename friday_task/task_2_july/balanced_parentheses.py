# balanced_parentheses.py

def is_balanced(expression):
    """
    Check if parentheses/brackets/braces are balanced.
    Uses stack: push opening, pop on closing — must match.
    """
    stack = Stack()
    matching = {')':'(', ']':'[', '}':'{'}
    openers  = set('([{')

    for char in expression:
        if char in openers:
            stack.push(char)           # Push every opener
        elif char in matching:
            if stack.is_empty():       # Closing with no opener
                return False
            if stack.pop() != matching[char]:  # Mismatch
                return False

    return stack.is_empty()   # True only if all openers were closed

tests = [
    '({[]})',
    '((()))',
    '([)]',
    '{[}',
    '',
]
for expr in tests:
    result = 'BALANCED ✅' if is_balanced(expr) else 'NOT BALANCED ❌'
    print(f'  {expr!r:<15} → {result}')