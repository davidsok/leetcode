def maxSetSize(riceBags):
    res = {}
    rb = sorted(riceBags)
    if not riceBags:
        print(-1)
        return -1
    for v in rb:
        res[v] = [v]
        for w in rb:
            if v ** 2 == w:
                res[v].append(w)
            if res[v][-1] ** 2 == w:
                res[v].append(w)
    print(res)       
    ans = max(len(x)for x in list(res.values()))
    print(ans)
    return ans
maxSetSize([625,4,2,5,25,26])  # OUTPUT = 3
maxSetSize([625,16,4,2,25,256,65536]) # OUTPUT = 5
maxSetSize([5,4,2,15,25])   #OUPUT = 2
maxSetSize([3,9,81,6561, 1, 2]) #OUTPUT 4
maxSetSize([])       #OUTPUT -1