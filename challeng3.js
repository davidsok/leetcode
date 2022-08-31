// Input: String="aabdec", Pattern="abc"
// Output: "abdec"
// Explanation: The smallest substring having all characters of the pattern is "abdec"

// Input: String="aabdec", Pattern="abac"
// Output: "aabdec"
// Explanation: The smallest substring having all characters occurrences of the pattern is "aabdec"

function challenge3(s, pattern) {
    let windowStart = 0,
        matchCount = 0,
        minLength = s.length + 1;
        subStart = 0;
    const patternMap = {};

    for (let v of pattern) {
        if (!(v in patternMap)) {
            patternMap[v] = 0
        }
        patternMap[v]++;
    }

    // console.log(patternMap);

    for (let windowEnd = 0; windowEnd < s.length; windowEnd++) {
        let rightChar = s[windowEnd];
        if (rightChar in patternMap) {
            patternMap[rightChar]--;
            if (patternMap[rightChar] >= 0) {
                matchCount++;
                console.log('match', matchCount);
            }
        }

        while (matchCount === pattern.length) {
            if (minLength >= windowEnd - windowStart + 1) {
                minLength = windowEnd - windowStart + 1;
                subStart = windowStart;
            }

            let leftChar = s[windowStart];
            windowStart++;
            if (leftChar in patternMap) {
                if(patternMap[leftChar] === 0) {
                    matchCount--;
                }
                patternMap[leftChar]++;
            }
        }
        
        

    }
    console.log('match', matchCount);
    return minLength > s.length ? "" : s.substring(subStart, subStart + minLength)
}

console.log(challenge3('aabdec', 'abc'))
console.log(challenge3('aabdec', 'abac'))