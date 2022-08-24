from sys import stdin , setrecursionlimit
input = stdin.readline
setrecursionlimit(5 * (10 ** 5))
inp = lambda : list(map(int, input().split()))
mod = 998244353
def add(a , b):return ((a % mod) + (b % mod)) % mod
def mul(a , b):return ((a % mod) * (b % mod)) % mod
def dfs(p , prev):
    global value
    count = 0
    for i in child[p]:
        if i[0] == prev: continue
        c = dfs(i[0] , p)
        value += c * (total - c) * i[1]
        count += c
    subtree[p] = count + 1
    return count + 1
def dfs1(p , prev , full):
    global value , best
    for i in child[p]:
        if i[0] == prev: continue
        toadd = (full - subtree[i[0]]) * (total - (full - subtree[i[0]])) * i[1]
        tosub = (subtree[i[0]] * (total - subtree[i[0]])) * i[1]
        value += toadd
        value -= tosub
        best = min(best , value)
        dfs1(i[0] , p , full)
        value -= toadd
        value += tosub
for T in range(1):
    n = int(input())
    m = []
    edges = []
    for i in range(n):
        m.append(int(input()))
        e = []
        for j in range(m[i] - 1):
            u , v , w = inp()
            e.append([u , v , w])
        edges.append(e)
    a = inp()
    total = sum(m)
    p = [2 , 1]
    ans = 0
    for i in range(n):
        child = [[] for i in range(m[i] + 1)]
        for x in edges[i]:
            u , v , w = x
            child[u].append([v , w])
            child[v].append([u , w])
        subtree = [0 for j in range(m[i] + 1)]
        value = 0
        dfs(1 , -1)
        best = value
        dfs1(1 , -1 , m[i])
        ans = add(ans , best)
    m.sort()
    a.sort(reverse = True)
    for i in range(n - 1):
        ans = add(ans , m[i] * (total - m[i]) * a[i])
    print(ans)