def miniMaxSum(arr):
    min_arr = sorted(arr)[:-1]
    max_arr = sorted(arr,reverse=True)[:-1]
    print(sum(min_arr), sum(max_arr))
    return sum(min_arr), sum(max_arr)

miniMaxSum([1,3,5,7,9])
