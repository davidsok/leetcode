# Problem Challenge 1: Permutation in a String (hard)

# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.

def challenge(s, pattern) -> bool:
    pattern_dict = {}
    matchCount = 0
    window_start = 0
    for v in pattern:
        if v not in pattern_dict:
            pattern_dict[v] = 0
        pattern_dict[v] += 1

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char in pattern_dict:
            pattern_dict[right_char] -= 1
            if pattern_dict[right_char] == 0:
                matchCount += 1
        
        if matchCount == len(pattern_dict):
            return True
        
        # shrinking window
        if window_end >= len(pattern) - 1:
            left_char = s[window_start]
            window_start += 1
            if left_char in pattern_dict:
                if pattern_dict[left_char] == 0:
                    matchCount -= 1  # Before putting the character back, decrement the matched count
                pattern_dict[left_char] += 1  # Put the character back
                
    return False


print(challenge("ppqp", "pq"))
print(challenge("abbcabc", "abcd"))