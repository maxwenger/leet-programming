import pytest
import math

# Given a sorted array of distinct integers and a target value, return the
# index if the target is found. If not, return the index where it would be
# if it were inserted in order

# nums: array of sorted ints
# target: number we are looking for

def brute_force(nums, target):
    if target <= nums[0]:
        return 0
    if target >= nums[-1]:
        return len(nums)

    for i in range(len(nums) - 1):
        if nums[i + 1] >= target:
            return i + 1

    raise ValueError("no solution")

def binary_search(nums, target):
    if target >= nums[-1]:
        return len(nums)

    low, high = 0, len(nums) - 1

    while low < high:

        ## // does int division. 5 // 2 = 2
        mid = (low + high) // 2

        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid

    return low

test_data = [
    ([1,3,5,6], 5, 2),
    ([1,3,5,6], 2, 1),
    ([1,3,5,6], 7, 4),
    ([1,3,5,6], 0, 0),
    ([1], 0, 0),
]

@pytest.mark.parametrize("nums,target,expected", test_data)
def test_brute_force(nums, target, expected):
    assert brute_force(nums, target) == expected

@pytest.mark.parametrize("nums,target,expected", test_data)
def test_binary_search(nums, target, expected):
    assert binary_search(nums, target) == expected
