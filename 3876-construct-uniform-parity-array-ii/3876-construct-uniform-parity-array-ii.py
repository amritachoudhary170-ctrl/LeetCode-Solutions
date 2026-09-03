class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums = min((x for x in nums1 if x % 2 == 1), default = None)

        if nums is None:
            return True

        for x in nums1:
            if x % 2 == 0 and x < nums:
                return False

        return True