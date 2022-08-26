def maxSumSubarray(arr, k):
    if k > len(arr):
        print(-1)
        return -1
    start_idx = 0
    end_idx = k + 1
    window_sum = []
    for i in range(start_idx, end_idx):
        window_sum.append(sum(arr[i:i+k]))
    ans = max(window_sum)
    print(ans)
    return ans

 
    

maxSumSubarray([2, 1, 5, 1, 3, 2], k=8)