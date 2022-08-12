from typing import DefaultDict


def topFrequent(nums: list[int], k: int) -> list[int]:
    res = DefaultDict()
    ans = []
    for v in nums:
        if v not in res:
            res[v] = []
        res[v].append(v)
    for i, v in res.items():
        print(len(v), v)
        for i in range(1, k+1):
            print(i)
            

        
    

topFrequent([1,1,1,2,2,3], 2)



# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
