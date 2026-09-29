class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        res = 0
        dup = set()
        for num in nums:
            if num in dup:
                res ^= num
            else:
                dup.add(num)
            
        return res