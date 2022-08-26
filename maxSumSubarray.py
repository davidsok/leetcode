def maxSumSubarray(arr, k):
    # window_sum, max_sum = 0,0 
    if k > len(arr):
        return -1
    max_sum = 0
    output = []
    for i in range( len(arr)):
        
        max_sum = sum(arr[i:i+k])
        output.append(max_sum)
    

maxSumSubarray([2, 1, 5, 1, 3, 2], k=3)