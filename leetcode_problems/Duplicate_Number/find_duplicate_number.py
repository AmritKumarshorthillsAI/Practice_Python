from typing import List

def find_duplicate(nums: List[int]) -> int:
    # Initialize the slow and fast pointers
    slow = nums[0]
    fast = nums[0]
    
    # Move slow pointer by one step and fast pointer by two steps
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Reset one pointer and move both by one step to find the entrance to the cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow
