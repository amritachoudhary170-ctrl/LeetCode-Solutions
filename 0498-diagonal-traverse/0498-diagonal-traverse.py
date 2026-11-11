class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if not mat or not mat[0]:
            return []

        m = len(mat)
        n = len(mat[0])

        result = []

        r = 0
        c = 0
        direction = 1

        for _ in range(m * n):

            result.append(mat[r][c])

            if direction == 1:

                if c == n - 1:
                    r += 1
                    direction = -1

                elif r == 0:
                    c += 1
                    direction = -1

                else:
                    r -= 1
                    c += 1

            else:

                if r == m - 1:
                    c += 1
                    direction = 1

                elif c == 0:
                    r += 1
                    direction = 1

                else:
                    r += 1
                    c -= 1

        return result