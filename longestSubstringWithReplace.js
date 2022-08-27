// Input: String="aabccbb", k=2
// Output: 5
// Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

function longestSubstringWReplace(s, k) {
    let windowStart = 0,
        windowLength = 0,
        charCount = 0;
    let charMap = {};

    for (let windowEnd = 0; windowEnd < s.length; windowEnd++) {
        let rightChar = s[windowEnd]
        if (!(rightChar in charMap)) {
            charMap[rightChar] = 0;
        }
        charMap[rightChar]++;
        charCount = Math.max(charCount, charMap[rightChar]);
        if ((windowEnd - windowStart + 1) - charCount > k) {
            let leftChar = s[windowStart];
            charMap[leftChar]--;
            windowStart++; // THIS LINE
        }
        windowLength = Math.max(windowEnd - windowStart + 1, windowLength);
    }
    return windowLength;
}

console.log(longestSubstringWReplace('aabccbbaa', 2));
console.log(longestSubstringWReplace('abbcbb', 1));