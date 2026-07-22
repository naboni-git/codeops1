import random

# =====================================================================
# 1. Recursive Sum & Countdown
# =====================================================================
def recursive_total(nums):
    # Base Case: If the list is empty, the sum is 0
    if len(nums) == 0:
        return 0
    # Recursive Case: Take the first number and add the sum of the rest
    return nums[0] + recursive_total(nums[1:])

def count_down(n):
    # Base Case: Stop when we hit 0
    if n <= 0:
        return
    print(n)
    # Recursive Case: Call itself with n - 1
    count_down(n - 1)


# =====================================================================
# 2. Binary Search (On sorted balances)
# =====================================================================
def binary_search(items, target):
    low = 0
    high = len(items) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid  # Return the index where we found it
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Return -1 if it doesn't exist


# =====================================================================
# 3. Merge Sort
# =====================================================================
def merge_sort(items):
    # Base Case: A list of 0 or 1 items is already sorted
    if len(items) <= 1:
        return items
        
    # Split the list in half
    mid = len(items) // 2
    left_half = merge_sort(items[:mid])
    right_half = merge_sort(items[mid:])
    
    # Merge the sorted halves back together
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = 0  # Pointer for left list
    j = 0  # Pointer for right list
    
    # Walk through both lists and compare elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
            
    # Add any remaining elements left over
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


# =====================================================================
# 4. Sort with a Key (Descending Balances)
# =====================================================================
# Given a list of (name, balance) tuples, sort by balance descending
def sort_by_balance(tuples_list):
    # We use key=lambda x: x[1] to sort specifically by the balance (index 1)
    return sorted(tuples_list, key=lambda x: x[1], reverse=True)


# =====================================================================
# 5. Two Pointers (Find pair that sums to target)
# =====================================================================
def has_pair(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1  # Sum is too small, move left pointer rightward
        else:
            right -= 1  # Sum is too big, move right pointer leftward
    return False


# =====================================================================
# TEST RUNS (To see outputs on screen)
# =====================================================================
if __name__ == "__main__":
    print("--- 1. Recursion ---")
    print("Recursive sum of [1, 2, 3, 4, 5]:", recursive_total([1, 2, 3, 4, 5]))
    print("Countdown from 3:")
    count_down(3)

    print("\n--- 2. Binary Search ---")
    balances = [200, 500, 1200, 1500, 4500]  # MUST BE SORTED
    print("Index of 1200:", binary_search(balances, 1200))
    print("Index of 9999:", binary_search(balances, 9999))

    print("\n--- 3. Merge Sort ---")
    random_list = [38, 27, 43, 3, 9, 82, 10]
    my_sorted = merge_sort(random_list)
    print("Merge Sorted list:", my_sorted)
    print("Matches Python's sorted()? ", my_sorted == sorted(random_list))

    print("\n--- 4. Sort with Key (Descending) ---")
    customers = [("Almaz", 1500), ("Dawit", 700), ("Tigist", 2200)]
    print(sort_by_balance(customers))

    print("\n--- 5. Two Pointers ---")
    sorted_numbers = [1, 2, 4, 6, 8, 9]  # MUST BE SORTED
    print("Do two numbers sum to 10?", has_pair(sorted_numbers, 10))  # True (4 + 6 or 2 + 8)
    print("Do two numbers sum to 13?", has_pair(sorted_numbers, 13))  # True (4 + 9)
    print("Do two numbers sum to 25?", has_pair(sorted_numbers, 25))  # False