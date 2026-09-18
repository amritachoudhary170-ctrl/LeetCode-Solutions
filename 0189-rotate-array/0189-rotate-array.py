class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k!=0:
            # left     right
            nums[:k], nums[k:] = nums[-k:], nums[:-k]

           
