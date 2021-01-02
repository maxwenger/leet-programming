import pytest

# nums: int array
# returns the sum of the largest subarray

def brute_force(nums, add=1):

    digit_index = 0
    while add != 0:
        digit_index += 1
        digit_add = add % 10
        add = add // 10

        if digit_index > len(nums):
           nums.insert(0, digit_add)
        else:
            digit_sum = nums[len(nums) - digit_index]
            digit_sum += digit_add

            ones_place = digit_sum % 10
            tens_place = digit_sum // 10

            nums[len(nums) - digit_index] = ones_place

            add += tens_place


    return nums

        


test_data = [
        ([1,2,3], [1,2,4]),
        ([4,3,2,1], [4,3,2,2]),
        ([0], [1]),
        ([9], [1,0]),
        ([8,9], [9,0]),
        ([9,9], [1,0,0]),
]

@pytest.mark.parametrize("nums,expected", test_data)
def test_brute_force(nums, expected):
    assert brute_force(nums) == expected

