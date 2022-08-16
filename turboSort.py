T = int(input()) # Number of elements
result = []
for _ in range(T):
    N = int(input())
    result.append(N)
for v in sorted(result):
    print(v)
