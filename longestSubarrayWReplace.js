
// Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
// Output: 6
// Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

function longestArrayWReplacement(arr, k) {
    let windowStart = 0,
        windowLength = 0,
        count = 0;
    for (let windowEnd = 0; windowEnd < arr.length; windowEnd++) {
        if (arr[windowEnd] === 1) {
            count++;
        }
        if ((windowEnd - windowStart + 1) - count > k) {
            if (arr[windowStart]  === 1) {
                count--;
            }
            windowStart++;
        } 
        windowLength = Math.max(windowLength, windowEnd - windowStart + 1);
    }
    return windowLength;
}

console.log(longestArrayWReplacement([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2));