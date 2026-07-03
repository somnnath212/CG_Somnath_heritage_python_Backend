stack = []

text = ""

# Type A
text += "A"
stack.append(text)

# Type B
text += "B"
stack.append(text)

# Type C
text += "C"
stack.append(text)

# Undo
stack.pop()
text = stack[-1]

# Undo
stack.pop()
text = stack[-1]

print("Final Text:", text)