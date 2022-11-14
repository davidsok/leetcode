def anagram(string, target) -> bool:
    result = {}
    for val in string:
        if val not in result:
            result[val] = 0
        result[val] += 1
    print(result)
    for v in target:
        if v not in result:
            return False
        result[v] -= 1

    print(result)
    for i in result:
        if result[i] != 0:
            return False

    return True

print(anagram("star", "stra"))