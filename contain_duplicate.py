from typing import DefaultDict

def containDuplicate(nums: list) -> bool:
    res = DefaultDict()
    for num in nums:
        tup = num
        if tup not in res:
            res[tup] = []
        res[tup].append(num)
    if len(res[tup]) > 1:
        return True
    return False

# Time Complexity = O(nlog(n))
# Space Complexity = O(n)

print(containDuplicate([1,2,3,2]))


#VS

def containDuplicate2(nums: list) -> bool:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
# Time Complexity = O(n^2)
# Space Complexity = O(1)

print(containDuplicate2([1,2,3,4]))    