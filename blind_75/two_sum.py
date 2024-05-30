
def twoSum(nums, target):
    """
    Given an array of integers and an integer target, 
    return indices of the two numbers such that they add up to the given target.
    """
    num_dict = {}
    for i, num in enumerate(nums):
        if num in num_dict:
            return [num_dict[num], i]
        else:
            num_dict[target - num] = i
    return []

