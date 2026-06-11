# Personal monthly budget tracker 

monthly_balance = 50000.00   # Starting balance 

 

# Income 

monthly_balance += 5000     # Freelance bonus 

 

# Expenses 

monthly_balance -= 12000    # Rent 

monthly_balance -= 4500     # Groceries 

monthly_balance -= 2200     # Electricity & Internet 

monthly_balance -= 3500     # Transport 

monthly_balance -= 1800     # Entertainment 

 

# Savings multiplier — invest remainder at 1.005% monthly return 

monthly_balance *= 1.005 

 

print(f'End-of-month balance: ₹{monthly_balance:.2f}') 

# Output: ₹31155.50 