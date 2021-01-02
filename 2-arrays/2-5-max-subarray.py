import pytest

# nums: int array
# returns the sum of the largest subarray

# N^2
def brute_force(nums):

    max_sum = nums[0]

    for i in range(len(nums) - 1):
        curr_sum = 0
        for j in range(i, len(nums) - 1):
            curr_sum += nums[j]
            max_sum = max(max_sum, curr_sum)

    return max_sum

# N
def kadane(nums):
    s = 0
    max_sum = nums[0]

    for n in nums:
        s = max(n, n + s)
        max_sum = max(s, max_sum)

    return max_sum
        

test_data = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([0], 0),
        ([-1], -1),
        ([-2147483647], -2147483647),
]

@pytest.mark.parametrize("nums,expected", test_data)
def test_brute_force(nums, expected):
    assert brute_force(nums) == expected

@pytest.mark.parametrize("nums,expected", test_data)
def test_kadane(nums, expected):
    assert kadane(nums) == expected
