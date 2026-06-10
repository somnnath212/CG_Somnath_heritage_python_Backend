city  = "Hyderabad"
temp  = 38.7
humid = 72

# Basic embedding
print(f"Weather in {city}: {temp}°C, humidity {humid}%")

# Expressions inside {}
print(f"Feels like: {temp + humid * 0.1:.1f}°C")

# Function calls inside {}
name = "   srinivas   "
print(f"Welcome, {name.strip().title()}!")
# Boolean check inside {}
marks = 75
print(f"Status: {'Pass' if marks >= 35 else 'Fail'}")
