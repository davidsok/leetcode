# L1 = [1,2,3]
# L1.extend([4,5])
# L1.extend([1,6,7,8])
# print(sorted(L1))


def combineAndSort(nums1: list[int], nums2: list[int]) -> list[int]:
    nums1.extend(nums2)
    return sorted(nums1)


nums1 = [1,2,3]
nums2 = [1,5,6,10,9]

print(combineAndSort(nums1, nums2))
