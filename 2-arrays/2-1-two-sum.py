import pytest

# nums: array of unique numbers
# target: sum of the two numbers we are looking for
# returns: indices of the two numbers that sum to the target


def brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    raise ValueError("No solution found!")

def hash_table(nums, target):
    nums_table = {}

    for i in range(len(nums)):
        nums_table[nums[i]] = i

    for i in  range(len(nums)):
        looking_for = target - nums[i]

        if looking_for in nums_table and looking_for != nums[i]:
            return [i, nums_table[looking_for]]

    raise ValueError("No solution found!")

def sort_method(nums, target):
    nums_list = []

    # Make a list of numbers, preserving the original index after a sort
    for i in range(len(nums)):
        nums_list.append([nums[i], i])

    nums_list.sort(key=lambda x: x[0])

    left = 0
    right = len(nums) - 1

    while left < right:
        curr_sum = nums_list[left][0] + nums_list[right][0]

        if curr_sum < target:
            left += 1
        elif curr_sum > target:
            right -= 1
        else:
            l = nums_list[left][1]
            r = nums_list[right][1]
            return [l, r]


    raise ValueError("No solution found!")


test_data = [
    ([2,7,11,15], 9, [0,1]),
    ([3,2,4], 6, [1,2]),
    ([2,7,11,15], 9, [0, 1])
]

@pytest.mark.parametrize("nums,target,expected", test_data)
def test_brute_force(nums, target, expected):
    assert brute_force(nums, target) == expected

@pytest.mark.parametrize("nums,target,expected", test_data)
def test_hash_table(nums, target, expected):
    assert hash_table(nums, target) == expected

@pytest.mark.parametrize("nums,target,expected", test_data)
def test_sort_method(nums, target, expected):
    assert sort_method(nums, target) == expected
