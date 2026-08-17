class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        
        if suits[0] == suits[1] == suits[2] == suits[3] == suits[4]:
            return "Flush"

        count = {}

        for rank in ranks:
            if rank in count:
                count[rank] += 1

            else:
                count[rank] = 1

        for rank in count:
            if count[rank] >= 3:
                return "Three of a Kind"

        for rank in count:
            if count[rank] >= 2:
                return "Pair"

            
        return "High Card"