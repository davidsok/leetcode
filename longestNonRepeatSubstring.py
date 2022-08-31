# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring with distinct characters is "abc".

def longestSubstring(s):
    s_dict = {}
    max_sub = 0
    for v in s:
        if v not in s_dict:
            s_dict[v] = 0
        s_dict[v] += 1
        
    max_sub = len(s_dict)
    return max_sub

print(longestSubstring('aabccbb'))
print(longestSubstring('abbbb'))