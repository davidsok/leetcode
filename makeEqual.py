t = int(input())
for _ in range(t):
    a,b = map(int, input().split())
    output = 'NO'
    if a > b:
        while (a > b):
            b = b * 2 
    elif a < b:
        while (b > a):
            a = a * 2
    if a == b:
        output = 'YES'
    print(output)