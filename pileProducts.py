def findMaxProducts(products):
    minIndex = int(input())
    maxIndex = int(input())
    output = []
    if maxIndex > len(products):
        return 0
    current = products[maxIndex]
    output.append(current)
    for i in range(maxIndex, minIndex, -1):
        if products[i-1] > current:
            output.append(current - 1)
            current = output[len(output)-1]
        else:
            current = products[i-1]
            output.append(current-1)
            current = output[len(output)-1]
    print(output)
    return output

products = [2, 9, 4, 7, 5, 2]   
findMaxProducts(products)
