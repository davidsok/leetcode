# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.

def permutationInString(s, pattern) -> bool:
    char_map = {}
    window_start = 0
    matched = 0
    for v in pattern:
        if v not in char_map:
            char_map[v] = 0
        char_map[v] += 1
    
    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char in char_map:
            char_map[right_char] -= 1
            if char_map[right_char] == 0:
                matched += 1

        if (window_end - window_start + 1) - 

    return False


console.log(permutationInString('oidbcaf', 'abc'))
console.log(permutationInString('bcdxabcdy', 'bcdyabcdx'))
console.log(permutationInString('aaaccbb', 'abc'))