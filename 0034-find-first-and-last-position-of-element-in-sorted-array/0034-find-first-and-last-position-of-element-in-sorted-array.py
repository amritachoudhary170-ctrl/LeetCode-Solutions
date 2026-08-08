class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findlast(nums, target):
            low = 0
            high = len(nums) -1
            last = -1
            while low <= high:
                mid = low + ( high - low) // 2

                if target == nums[mid]:
                    last = mid
                    low = mid + 1
                elif target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid +1
            return last

        def findfirst(nums, target):
            low = 0
            high = len(nums) -1
            first = -1

            while low <= high:
                mid = (low + high) // 2

                if target == nums[mid]:
                    first = mid
                    high = mid - 1

                elif target > nums[mid]:
                    low = mid + 1

                else:
                    high = mid - 1

            return first

        first = findfirst(nums, target)
        last = findlast(nums, target)

        result = [first, last]
        return result 