from typing import List

# My first solution:
def my_has_duplicate(self, nums: List[int]) -> bool:

    duplicates = dict()
    for e in nums:
        if duplicates.get(str(e)) is None:
            duplicates.update({str(e): 1})
        else:
            return True
    return False

# Other solutions:

# Hash Set Length
def has_duplicate_1(self, nums: List[int]) -> bool:
    return len(set(nums)) < len(nums)

# Hash Set
def has_duplicate_2(self, nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False