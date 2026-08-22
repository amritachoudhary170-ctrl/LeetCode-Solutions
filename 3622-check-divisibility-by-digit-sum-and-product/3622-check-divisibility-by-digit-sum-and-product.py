class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original = n
        digit_sum = 0
        product = 1

        while n > 0:
            digit = n % 10

            digit_sum += digit
            product *= digit

            n = n // 10

        return original % (digit_sum + product) == 0