class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        num = 0
        sign = 1
        i = 0

        while i < len(s) and s[i] == ' ' :
            i += 1

        if i < len(s) and s[i] == '-':
            sign = -1
            i += 1

        elif i < len(s) and s[i] == '+':
            i += 1

        while i < len(s) and s[i].isdigit():
            num = num*10 + int(s[i])
            i += 1

        result = num*sign

        if result < -2**31:
            return -2**31

        if result > 2**31 - 1:
            return 2**31 - 1

        return result