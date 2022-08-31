# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

def longestArrayWReplace(arr, k) -> int:
    window_start, count, window_length = 0, 0, 0
    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            count += 1
        if window_end - window_start + 1 - count > k:
            if arr[window_start] == 1:
                count -= 1
            window_start += 1
        window_length = max(window_length, window_end - window_start+1)
    return window_length

print(longestArrayWReplace([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
