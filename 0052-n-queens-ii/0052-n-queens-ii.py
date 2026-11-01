class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDig = set()
        negDig = set()
        count = 0

        def backtrack(r):
            nonlocal count

            if r == n :
                count += 1
                return

            for c in range(n):

                if c in col or (r + c) in posDig or (r - c) in negDig:
                    continue

                
                col.add(c)
                posDig.add(r + c)
                negDig.add(r - c)

                backtrack(r + 1)

                col.remove(c)
                posDig.remove(r + c)
                negDig.remove(r - c)
        backtrack(0)
        return count