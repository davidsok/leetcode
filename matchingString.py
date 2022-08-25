def matchingStrings(strings, queries):
    queries_dict = {}
    output = []
    for v in strings:
        # print(v)
        # print(strings)
        # print(queries)
        if v in queries_dict:
            queries_dict[v] += 1
        else:
            queries_dict[v] = 1
    # print(queries_dict)
    for w in queries:
        if w in queries_dict:
            output.append(queries_dict[w])
        else:
            output.append(0)
    print(output)
    return output
    

strings = ['ab', 'ab', 'abc']
# strings = ['aba', 'aba', 'baba']
# queries = ['aba', 'baba', 'aba', 'zxzb']
# queries = ['aba', 'xzxb','ab']
queries = ['ab', 'abc','bc']
# queries = ['abc', 'sdaklfj', 'asdjf', 'na', 'basdn']
# queries = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf', 'na', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf']


print(matchingStrings(strings, queries))