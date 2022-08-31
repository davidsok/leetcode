def lonelyinteger(a):
    result_dict = {}
    for v in a:
        if  v not in result_dict:
            result_dict[v] = 1
        else:
            result_dict[v] += 1
    for key, value in result_dict.items():
        if value == 1:
            print(key)
            return key
    return None

lonelyinteger([1,2,3,4,5,3,2,1])
lonelyinteger([34,95,34,64,45,95,16,80,80,75,3,25,75,25,31,3,64,16,31])
