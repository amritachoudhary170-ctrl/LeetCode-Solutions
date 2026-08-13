class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup = set()
        left = 0
        ans = 0

        for i in range(len(s)):

            while s[i] in dup:
                dup.remove(s[left])
                left += 1
            
            dup.add(s[i])

            ans = max(ans, i - left + 1)

        return ans