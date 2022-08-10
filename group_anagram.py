from typing import DefaultDict
def groupAnagram(strs: list[str]) -> list[list[str]]:
        res = DefaultDict()
        for string in strs:
            sorted_string = tuple(sorted(string))
            if sorted_string not in res:
                res[sorted_string] = []
            res[sorted_string].append(string)
        print(list(res.values()))
        return list(res.values())
# Time complexity: O(m*nlogn))
# Space complexity: O(n)

groupAnagram(["eat","tea","tan","ate","nat","bat"])
