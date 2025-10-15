from typing import List

def twoSum(nums: List[int], target: int) ->List[int]:
    checked_value = {}
    for i, value in enumerate(nums):
        num = target - value
        if num in checked_value:
            return [checked_value[num], i]
        checked_value[value] = i