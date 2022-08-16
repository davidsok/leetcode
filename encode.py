def encode(input: str) -> str:
    if not input:
        return 'INPUT EMPTY'
    count = 0
    output = ''
    prev_char = ''
    for v in input:
        if v == prev_char:
            count += 1
            prev_char = v
        else:
            if prev_char != '':
                output += str(count)+ prev_char
            count = 1
            prev_char = v
    output += str(count)+ prev_char
    return output



#input = 'aaaabbccc'
# output = '4a2b3c'
print(encode(input))