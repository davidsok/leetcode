def maxSumSubarray(arr, k):
    if k > len(arr):
        print(-1)
        return -1
    start_window = 0
    end_window = k + 1
    window_sum = []
    for i in range(start_window, end_window):
        window_sum.append(sum(arr[i:i+k]))
    ans = max(window_sum)
    print(f'max sum of {k} index of {arr} is {ans}')
    return ans

 

def max_sub_array_of_size_k(arr, k):
    max_sum, window_sum = 0, 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # add the next element
        # slide the window, no need to slide if we've not hit the required window size of 'k'
        if window_end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]  # subtract the element going out
            window_start += 1  # slide the window ahead
    return max_sum
    

maxSumSubarray([2, 1, 5, 1, 3, 2], k=3)
print(max_sub_array_of_size_k([2, 1, 5, 1, 3, 2], 3))