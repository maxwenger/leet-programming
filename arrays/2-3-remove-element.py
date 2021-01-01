import pytest

# nums: array of numbers
# val: value to remove, in place
# returns: new length of array

def two_pointers(nums, val):

    i = 0
    while i < len(nums):
        if nums[i] == val:
            del nums[i]
        else:
            i += 1

    return len(nums)

def sorting(nums, val):
    nums.sort()

    left = 0
    right = len(nums) - 1

    while nums[left] != val and nums[right] != val and right >= left:
        if nums[left] != val:
            left += 1

        if nums[right] != val:
            right -= 1

    del nums[left:right]

    return len(nums)



test_data = [
        ([3,2,2,3], 3, 2),
        ([0,1,2,2,3,0,4,2], 2, 5)
]

@pytest.mark.parametrize("nums,val,expected", test_data)
def test_two_pointers(nums, val, expected):
    assert two_pointers(nums, val) == expected

@pytest.mark.parametrize("nums,val,expected", test_data)
def test_sorting(nums, val, expected):
    assert sorting(nums, val) == expected
