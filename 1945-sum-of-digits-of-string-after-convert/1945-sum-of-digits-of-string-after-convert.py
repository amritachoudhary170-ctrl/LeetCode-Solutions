class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ""

        for ch in s:
            num += str(ord(ch) - ord('a') + 1)

        num = int(num)

        for i in range(k):
            total = 0

            while num > 0 :
                total += num % 10
                num //= 10

            num = total

        return num
