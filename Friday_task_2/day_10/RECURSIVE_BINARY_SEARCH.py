def binary_search_recursive(arr, target, left, right): 

    # BASE CASE 1: Search space exhausted 

    if left > right: 

        return -1 

  

    mid = (left + right) // 2 

  

    # BASE CASE 2: Target found 

    if arr[mid] == target: 

        return mid 

  

    # RECURSIVE CASE: Search appropriate half 

    elif arr[mid] < target: 

        return binary_search_recursive(arr, target, mid + 1, right) 

    else: 

        return binary_search_recursive(arr, target, left, mid - 1) 

  

# ── REAL-LIFE USE CASE: Find a student rank in sorted leaderboard ───── 

leaderboard = [1200, 1450, 1600, 1750, 1800, 1920, 2050, 2200] 

score_to_find = 1800 

  

pos = binary_search_recursive(leaderboard, score_to_find, 0, len(leaderboard)-1) 

print(f'Score {score_to_find} is at leaderboard rank {pos + 1}')