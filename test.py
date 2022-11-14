def newList(arr) -> list:
    new_list = []
    for i in range(len(arr)):
        if arr[i] >= arr[2]:
            new_list.append(arr[i])
    return new_list

print(newList([5,1,3,2,4]))