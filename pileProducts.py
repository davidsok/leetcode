def findMaxProducts(products, low, high):
    # minIndex = int(input())
    # maxIndex = int(input())
    output = []
    if high > len(products):
        return 0
    current = products[high]
    output.append(current)
    for i in range(high, low, -1):
        print('i', i, 'product', products[i-1])
        if products[i-1] == current:
            output.insert(0, current - 1)
            # current = output[len(output)-1]
        elif products[i-1] < current:
            current = products[i-1]
            output.insert(0,current)
            # current = output[len(output)-1]
        else:
            current = products[i]
            print('current 1= ', current)
            output.insert(0,current-1)
            # current = output[len(output)-1]
        print('current', current)
    print(output)
    return output

products = [2, 9, 4, 7, 5, 2]   
findMaxProducts(products, 1, 4)

# OUPUT = [2, 3, 4, 5]
