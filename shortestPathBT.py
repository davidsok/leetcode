n = int(input())
for _ in range(n):
    i,j = map(int, input().split())
    step = 0
    while i!= j:
        if i > j:
            step += 1
            i //= 2 #floor disivion (after increase step divide i by 2)
        else:
            step += 1
            j //= 2
    print(step)
