// function longestSubstring(s, k){
//     let dict = {};
//     let window_start = 0;
//     let window_length = -Infinity;
//     for (let window_end = 0 ; window_end < s.length ; window_end++){
//         let char = s[window_end];
//         if (char in dict) {
//             dict[char] += 1;
//         }
//         dict[char] = 1;
//         if (Object.keys(dict).length >= k) {
//             window_length = Math.max(window_length, window_end - window_start + 1);
//         }
//     }
//     return window_length;
// }

function longestSubstring(s, k) {
    let charMap = {}
    let windowStart = 0
    let windowLength = 0

    for(let windowEnd=0; windowEnd < s.length; windowEnd++) {
        let rightChar = s[windowEnd]

        if(!(rightChar in charMap)) {
            charMap[rightChar] = 0
        }
        charMap[rightChar] += 1
        console.log(charMap)
        while(Object.keys(charMap).length > k) {
            let leftChar = s[windowStart]
            charMap[leftChar] -= 1

            if (charMap[leftChar] === 0) {
                delete charMap[leftChar]
            }

            windowStart++
        }

        windowLength = Math.max(windowLength, windowEnd-windowStart+1)
    }

    return windowLength
}


console.log(`Length of the longest substring: `
    + longestSubstring('araaci', 2));
console.log(`Length of the longest substring: `
    + longestSubstring('araaci', 1));
console.log(`Length of the longest substring: `
    + longestSubstring('cbbebi', 3));