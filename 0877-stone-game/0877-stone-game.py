class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        return len(piles) % 2 == 0