// # Input: String="aabccbb"
// # Output: 3
// # Explanation: The longest substring with distinct characters is "abc".



function longestString(s) {
    const charMap = {}
    let windowStart = 0,
        windowLength = 0
    
    for(let windowEnd=0; windowEnd < s.length; windowEnd++){
        const rightChar = s[windowEnd]

        if (rightChar in charMap){
            windowStart = Math.max(windowStart, charMap[rightChar]+1)
        }
        charMap[rightChar] = windowEnd



        windowLength = Math.max(windowLength, windowEnd-windowStart+1)
    }
    
    return windowLength;
}


function longestString2(s) {
    const charMap = {};
    for (let v of s) {
        if (!(v in charMap)) {
            charMap[v] = 0;
        }
        charMap[v]++;
    }
    console.log(charMap);
    return Object.keys(charMap).length;

}

console.log(longestString2("aabccbb"));

console.log(longestString2("aabbbc"));