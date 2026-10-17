class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        result = []
        used = [False] * len(nums1)

        for num in nums2:
            left, right = 0, len(nums1) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums1[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1

            # Find the first unused occurrence
            for i in range(left, len(nums1)):
                if nums1[i] == num and not used[i]:
                    result.append(num)
                    used[i] = True
                    break
                if nums1[i] > num:
                    break

        return result