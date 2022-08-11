from typing import DefaultDict

def twoSum(nums: list, target) -> list:
    res = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                res.append(i)
                res.append(j)
    print(res)
    return res

twoSum([2,7,11,15], 9)    