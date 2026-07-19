class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if (m * k) > n:
            return -1
        def func(day):
            flowers, bouquets = 0, 0
            for i in bloomDay:
                if i <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m

        l, h = min(bloomDay), max(bloomDay)
        ans = float("inf")
        while l <=  h:
            mid = (l + h) // 2
            if func(mid):
                ans = min(ans, mid)
                h = mid - 1
            else:
                l = mid + 1
        
        return ans if ans != float("inf") else -1

        