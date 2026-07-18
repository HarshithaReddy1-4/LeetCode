class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def koko(m):
            total = 0
            for i in piles:
                total += math.ceil(i/m)
            return total
        ans = float("inf")
        low = 1
        high = max(piles)
        while low <= high:
            mid = (low + high) // 2
            k = koko(mid)
            if k > h:
                low = mid + 1
            else:
                ans = min(ans, mid)
                high = mid - 1
        return ans
    