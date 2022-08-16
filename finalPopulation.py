def finalPopulation() -> int:
    t = int(input())
    for _ in range(t):
        p = list(map(int, input().split(" ")))
        output = p[0] - p[1] + p[2]
        print(output)


finalPopulation()