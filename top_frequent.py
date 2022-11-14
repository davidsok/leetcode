from typing import DefaultDict


def topFrequent(nums: list[int], k: int) -> list[int]:
    res = DefaultDict()
    # ans = DefaultDict()
    output = []
    for v in nums:
        if v not in res:
            res[v] = 0
        res[v] += 1
    print(res)
    max_val = max(res.values())
    for i, v in res.items():
        if v > max_val - k:
            output.append(i)
    print(output)
    return output
            

        
    


topFrequent([1,1,1,2,2,3], 2)
topFrequent([1,1,1,2,2,3,3,3,3,4], 3)
topFrequent([1,1,1,2,2,3,4], 2)





# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Input: nums = [1,1,1,2,2,3,3,3,3,4], k = 3
# Output: [1,2,3]

# Input: nums = [1,1,1,2,2,3,4], k = 2
# Output: [1,2]
