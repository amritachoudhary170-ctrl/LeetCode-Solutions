class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        large = max(nums)
        index = nums.index(large)

        nums.remove(large)

        if all(large >= 2 * num for num in nums):
            return index
    
        return -1