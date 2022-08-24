def maxSetSize(riceBags):
    size = {}
    rb = sorted(riceBags)
    if not riceBags:
        return -1
    for i in range(len(rb)):
        print('i', i, 'riceBags', rb[i])
        print('size', size)
        
        
    print(size)
    # for i in range(len(riceBags)):
    #     for j in (range(i+1, len(riceBags))):
    #         if riceBags[i] ** 2 == riceBags[j]:
    #             set.append([riceBags[i],riceBags[j]])
    #         if riceBags[j] ** 2 == riceBags[i]:
    #             set.append([riceBags[i],riceBags[j]])
    #         if riceBags[j-1] ** 2 == riceBags[i] and riceBags[i] ** 2 == riceBags[j]:
    #             set.append([riceBags[i], riceBags[j-1], riceBags[j]])
    # print(set)
    # size = []
    # for i in range(len(set)):
    #     size.append(len(set[i]))
    return size
maxSetSize([625,4,2,5,25,26])

# maxSetSize([5,4,2,15,25])

def maxSetSize2(riceBags):
    box_dict = {}
    for num in riceBags:
        if num in box_dict:
            box_dict[num] += 1
        else:
            box_dict[num] = 1
    numArr = [(key,val) for key,val in box_dict.items()]

    