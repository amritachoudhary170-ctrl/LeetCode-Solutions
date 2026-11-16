class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res  = 0
        for ch in columnTitle:
            value = ord(ch) - ord('A') + 1
            res = res * 26 + value

        return res