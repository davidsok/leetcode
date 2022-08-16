T = int(input()) # Number of Test Cases
if 0 <= T <= 100^6:
    for _ in range(T):
        N = int(input()) # number to calculate
        result = 1
        if N == 0:
            result = 1
        elif 0 < N <= 100:
            for i in range(1, N+1):
                result *= i
        print(result)
