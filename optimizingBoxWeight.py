

def minimalHeaviestSetA(arr, n):
    pass
    # box_dict = {}
    # for num in arr:
    #     box_dict = 


minimalHeaviestSetA([3, 7, 5, 6, 2], 5)




# input: arr = [3, 7, 5, 6, 2] , n = 5
# The 2 subsets in arr that satisfy the conditions for A are [5, 7] and [6, 7] :

# A is minimal (size 2)
# Sum(A) = (5 + 7) = 12 > Sum(B) = (2 + 3 + 6) = 11
# Sum(A) = (6 + 7) = 13 > Sum(B) = (2 + 3 + 5) = 10
# The intersection of A and B is null and their union is equal to arr.
# The subset A where the sum of its weight is maximal is [6, 7]

# num_list = [(k, v) for k, v in box_dict.items()]

def optimizeBox(arr):
    box_dict = {}
    for val in arr:
        if val in box_dict:
            box_dict[val] += 1
        else:
            box_dict[val] = 1
    box_list = [(key, value) for key, value in box_dict.items()]
    box_list.sort(key = lambda x: (-x[0], -x[0]*x[1]))
    A = []
    B = arr
    print('A', A)
    print('B', B)
    current_weight = 0
    max_weight = sum(arr)
    for i,j in box_list:
        if current_weight + (i*j) < max_weight - current_weight:
            A.append(i*j)
            current_weight += i*j
            B.remove(i*j)
    print('A', A)
    print(B)
    return f'A = {A}'




def optimizeBox2(arr):
    box_dict = {}
    for num in arr:
        if num in box_dict:
            box_dict[num] += 1
        else:
            box_dict[num] = 1
    numArr = [(key,val) for key,val in box_dict.items()]

    numArr.sort(key = lambda x : (-x[0],-x[0]*x[1]))
    max_weight = sum(arr)
    A = []
    current_weight = 0
    for i , j in numArr:
        if current_weight + (i * j) < max_weight - current_weight:
            current_weight += (i * j)
            A += ([i] * j)
    if current_weight > max_weight-current_weight:
        return A
    else:
        return [x for x in arr if x not in A]

arr = [5,3,2,4,1,2]
n = 6
# arr = [3, 7, 5, 6, 2]
# n = 5
print(optimizeBox(arr))
