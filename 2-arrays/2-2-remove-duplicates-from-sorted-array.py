import pytest

# Remove duplicates in-memory
# nums: sorted array
# return: length of new array after removing duplicates

def brute_force(nums):

    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            del nums[i + 1]
        else:
            i += 1

    return len(nums)

def cheaky_way(nums):

    last = nums[0]
    num_unique = 1
    for i in nums:
        if last != i:
            num_unique += 1
            last = i

    return num_unique

test_data = [
    ([1,1,2], 2),
    ([0,0,1,1,1,2,2,3,3,4], 5)
]

@pytest.mark.parametrize("nums,expected", test_data)
def test_brute_force(nums, expected):
    assert brute_force(nums) == expected

@pytest.mark.parametrize("nums,expected", test_data)
def test_cheaky_way(nums, expected):
    assert cheaky_way(nums) == expected
