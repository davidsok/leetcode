from typing import DefaultDict

def containDuplicate(nums):
    res = DefaultDict()
    for num in nums:
        tup = num
        if tup not in res:
            res[tup] = []
        res[tup].append(num)
    print(res)
    if len(res[tup]) > 1:
        return True
    return False

print(containDuplicate([1,2,3,1]))