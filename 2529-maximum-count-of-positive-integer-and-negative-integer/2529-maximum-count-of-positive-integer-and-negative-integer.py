class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def totalpositive(nums):
            low = 0
            high = len(nums) - 1

            while low <= high:
                mid = low + (high - low)// 2

                if nums[mid] > 0:
                    high = mid - 1

                else:
                    low = mid + 1

            return len(nums) - low

        
        def totalnegative(nums):
            low = 0
            high = len(nums) - 1

            while low <= high:
                mid = low + (high - low)// 2

                if nums[mid] < 0:
                    low = mid + 1
                else:
                    high = mid - 1

            return low

        positive = totalpositive(nums)
        negative = totalnegative(nums)

        return max(positive, negative)