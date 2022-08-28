// Input: String="oidbcaf", Pattern="abc"
// Output: true
// Explanation: The string contains "bca" which is a permutation of the given pattern.

function permutationInString(s, pattern) {
    let patternMap = {};
    let windowStart = 0,
        matched = 0;

    for (v of pattern) {
        if (!(v in patternMap)) {
            patternMap[v] = 0;
        }
        patternMap[v]++;
    }
    // console.log(patternMap);

    for (let windowEnd = 0; windowEnd < s.length; windowEnd++) {
        let rightChar = s[windowEnd];
        if (rightChar in patternMap) {
            patternMap[rightChar]--;
            if (patternMap[rightChar] === 0){
                matched++;
            } 
        }

        if (matched === Object.keys(patternMap).length) {
            return true;
        }
        if (windowEnd >= pattern.length - 1) {
            let leftChar = s[windowStart];
            windowStart++;
            if (leftChar in patternMap) {
                if (patternMap[leftChar] === 0) {
                    matched--;
                }
                patternMap[leftChar]++;
            }
        }
    }
   
    return false;
}

console.log(permutationInString('oidbcaf', 'abc'))
console.log(permutationInString('bcdxabcdy', 'bcdyabcdx'))
console.log(permutationInString('aaaccbb', 'abc'))