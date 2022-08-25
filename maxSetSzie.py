def maxSetSize(riceBags):
    res = {}
    rb = sorted(riceBags)
    if not riceBags:
        return -1
    for i in range(len(rb)):
        res[rb[i]] = [rb[i]]
        for j in range(len(rb)):
            if rb[i] ** 2 == rb[j]:
                res[rb[i]].append(rb[j])
            if res[rb[i]][len(res[rb[i]])-1] ** 2 == rb[j]:
                res[rb[i]].append(rb[j])
           
    ans = max(len(x)for x in list(res.values()))
    print(ans)

    return ans
maxSetSize([625,4,2,5,25,26])
maxSetSize([625,16,4,2,25,256])
maxSetSize([5,4,2,15,25])    