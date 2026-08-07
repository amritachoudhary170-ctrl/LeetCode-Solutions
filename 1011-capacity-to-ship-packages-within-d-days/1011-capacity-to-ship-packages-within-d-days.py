class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(weights, days, capacity):
            currentweight = 0
            requireddays = 1

            for weight in weights:
                if currentweight + weight <= capacity:
                    currentweight += weight

                else:
                    requireddays += 1
                    currentweight = weight
            return requireddays <= days

        low = max(weights)
        high = sum(weights)
        ans = high 

        while low <= high:
            mid = (low + high) // 2

            if possible(weights, days, mid):
                ans = mid
                high = mid - 1

            else:
                low = mid + 1
        return ans 