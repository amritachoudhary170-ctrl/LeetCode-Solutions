class Solution:
    def climbStairs(self, n: int) -> int:
        back2 = 1
        back1 = 1

        for i in range(2, n+1):
            curr = back2 + back1 

            back2 = back1
            back1 = curr
            

        return back1