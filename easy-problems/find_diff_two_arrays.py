class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        result = []
        result.append(list(nums1-nums2))
        result.append(list(nums2-nums1))
        return result

    def findDifference_v_2(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        diff1 = list(set1 - set2)
        diff2 = list(set2 - set1)
        return [diff1, diff2]

    def findDifference_v_3(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1.difference(set2)), list(set2.difference(set1))]