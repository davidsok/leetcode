# Input: String="ppqp", Pattern="pq"
# Output: [1, 2]
# Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

# Input: String="abbcabc", Pattern="abc"
# Output: [2, 3, 4]
# Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".

def challenge2(s, pattern):
    window_start = 0
    match_count = 0
    output = []
    pattern_dict = {}

    for v in pattern:
        if v not in pattern_dict:
            pattern_dict[v] = 0
        pattern_dict[v] += 1
    
    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char in pattern_dict:
            pattern_dict[right_char] -= 1
            if pattern_dict[right_char] == 0:
                match_count += 1
            
        if match_count == len(pattern_dict):
            output.append(window_start)

        # Shrink window
        if window_end >= len(pattern) - 1:
            left_char = s[window_start]
            window_start += 1
            if left_char in pattern_dict:
                if pattern_dict[left_char] == 0:
                    match_count -= 1
                pattern_dict[left_char] += 1

    return output
                

print(challenge2('ppqp', 'pq'))
print(challenge2("abbcabc", "abc"))