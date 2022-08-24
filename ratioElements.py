def plusMinus(arr):
    p_count = 0
    n_count = 0
    z_count = 0
    for val in arr:
        if val > 0:
            p_count += 1
        elif val == 0:
            z_count +=1
        else:
            n_count += 1
    print(float("{:.6f}".format(p_count/len(arr))))
    print(float("{:.6f}".format(n_count/len(arr))))
    print(float("{:.6f}".format(z_count/len(arr))))
    return float("{:.6f}".format(p_count/len(arr))), float("{:.6f}".format(n_count/len(arr))), float("{:.6f}".format(z_count/len(arr)))

plusMinus([1, 1, 0, -1, -1])