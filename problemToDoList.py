T = int(input()) # number of Test Cases
if 0 <= T <= 1000:
    for _ in range(T):
        target = 1000 # target number
        N = int(input()) # number of elements per test case
        if 0 <= N <= 1000:
            P = list(map(int, input().split(" ")))[:N]
            output = 0
            for idx, value in enumerate(P):
                if 0<= value <= 5000 and value >= target:
                    output += 1
            print(output)
