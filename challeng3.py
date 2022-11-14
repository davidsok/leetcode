# // Input: String="aabdec", Pattern="abc"
# // Output: "abdec"
# // Explanation: The smallest substring having all characters of the pattern is "abdec"

# // Input: String="aabdec", Pattern="abac"
# // Output: "aabdec"
# // Explanation: The smallest substring having all characters occurrences of the pattern is "aabdec"

def challeng3(s, pattern):
    pattern_map = {}
    match_count = 0
    