//Problem Challenge 1: Permutation in a String (hard)

// Input: String="oidbcaf", Pattern="abc"
// Output: true
// Explanation: The string contains "bca" which is a permutation of the given pattern.

// { a: 1, b: 1, c: 1}

function permutation(s, pattern) {
    let windowStart = 0,
        matchCount = 0;
    const patternMap = {};

    for (v of pattern) {
        if (!(v in patternMap)) {
            patternMap[v] = 0
        }
        patternMap[v]++;
    }

    for (let windowEnd=0; windowEnd < s.length; windowEnd++) {
        let rightChar = s[windowEnd];
        if (rightChar in patternMap) {
            patternMap[rightChar]--;
            if (patternMap[rightChar] === 0) {
                matchCount++;
            }
        }

        if (matchCount === Object.keys(patternMap).length) {
            return true;
        }

        // shrink window

        if (windowEnd + 1 >= pattern.length) {
            let leftChar = s[windowStart];
            if (leftChar in patternMap) {
                if (patternMap[leftChar] === 0) {
                    matchCount--;
                }
                patternMap[leftChar]++;
            }
            windowStart++;
        }

    }
    return false;
}

console.log(permutation("oidbcaf", "abc"))
console.log(permutation("odicf", "dc"))