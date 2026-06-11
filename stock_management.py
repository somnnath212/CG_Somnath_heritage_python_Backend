# Warehouse inventory management 

stock_laptops = 100 

 

# Process orders throughout the day 

stock_laptops -= 12   # Morning batch 

stock_laptops -= 8    # Afternoon order 

stock_laptops -= 5    # Evening walk-in 

 

print(f'Remaining Laptops: {stock_laptops}')   # 75 

 

# Alert when stock is low 

if stock_laptops < 20: 

    print('Low stock alert! Reorder required.')