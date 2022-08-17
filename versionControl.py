# Input
# The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.

# The first line of the test case description contains three integers N, M and K denoting the number of source files in the project, the number of ignored source files and the number of tracked source files.

# The second line contains M distinct integers denoting the sequence A of ignored source files. The sequence is strictly increasing.

# The third line contains K distinct integers denoting the sequence B of tracked source files. The sequence is strictly increasing.

# Output
# For each test case, output a single line containing two integers: the number of the source files, that are both tracked and ignored, and the number of the source files, that are both untracked and unignored.

# Constraints
# 1 ≤ T ≤ 100
# 1 ≤ M, K ≤ N ≤ 100
# 1 ≤ A1 < A2 < ... < AM ≤ N
# 1 ≤ B1 < B2 < ... < BK ≤ N
# Sample 1:
# Input
# 2
# 7 4 6
# 1 4 6 7
# 1 2 3 4 6 7
# 4 2 2
# 1 4
# 3 4
# Output
# 4 1
# 1 1

t = int(input()) # test cases
for _ in range(t):
    n,m,k = map(int, input().split())
    a = list(map(int, input().split()))[:m]
    b = list(map(int, input().split()))[:k]
    source = list(range(1, n+1))
    track_ignore_count = 0
    untrack_unignore_count = 0
    for v in source:
        if v in a and v in b:
            track_ignore_count += 1
        if v not in a and v not in b:
            untrack_unignore_count += 1

    print(track_ignore_count, untrack_unignore_count)


