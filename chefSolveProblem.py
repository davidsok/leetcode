def chefSolveProblem():
    problem = 10
    output = 0
    weeks = list(map(int, input().split(" ")))
    for v in weeks:
        if v >= problem:
            output += 1
    print(output)



chefSolveProblem()

