# Shared apartment — split utility bill 

electricity_bill = 3600.00 

num_roommates    = 4 

 

electricity_bill /= num_roommates 

print(f'Each pays: ₹{electricity_bill:.2f}')   # ₹900.00 

 

# Normalize data — scale values to 0–1 range 

max_temperature = 45.0 

current_temp    = 36.0 

current_temp /= max_temperature 

print(f'Normalized temp: {current_temp:.2f}')   # 0.80