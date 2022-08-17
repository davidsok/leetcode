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

def encode2(input: str) -> str:
    if not input:
        return 'Input is empty!'
    out_dict = {}
    result = ''
    prev_char = ''
    for v in input:
        print(prev_char)
        if v in out_dict:
            out_dict[v] += 1
            prev_char = v
        else:
            out_dict[v] = 1
            prev_char = v
    print(out_dict)
    for key, value in out_dict.items():
        result += f'{value}{key}'
    return result

input = 'aaaabbccca'
# output = '4a2b3c'
# print(encode(input))
print(encode2(input))