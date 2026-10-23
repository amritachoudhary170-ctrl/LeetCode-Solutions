class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        num = set(nums)

        while original in num:
            original *= 2

        return original
