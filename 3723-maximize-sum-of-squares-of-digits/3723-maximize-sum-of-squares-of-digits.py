class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ''

        nines = sum // 9
        remain = sum % 9

        res = '9' * nines

        if remain > 0:
            res += str(remain)

        res += '0' * (num - len(res))

        return res
        

        