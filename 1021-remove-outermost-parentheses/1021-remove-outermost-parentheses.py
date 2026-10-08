class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        cnt = 0

        for ch in s:
            if ch == '(':
                if cnt > 0:
                    res += ch

                cnt += 1

            else:
                cnt -= 1
                if cnt > 0:
                    res += ch

        return res

