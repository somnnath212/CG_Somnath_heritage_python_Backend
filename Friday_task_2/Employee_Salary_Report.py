employees = {
    "Rahul": 50000,
    "Amit": 60000,
    "Priya": 55000,
    "Neha": 70000
}

salaries = list(employees.values())

print("Highest Salary:", max(salaries))
print("Lowest Salary:", min(salaries))
print("Average Salary:", sum(salaries) / len(salaries))