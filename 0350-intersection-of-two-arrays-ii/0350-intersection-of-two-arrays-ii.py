class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        dict_uniq = Counter(nums1) & Counter(nums2)
        return list(dict_uniq.elements())
        