class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def func(target):
            s = 0
            day = 0
            i = 0
            while i < len(weights):
                s += weights[i]
                if s >= target:
                    day += 1
                    if s == target:
                        i += 1
                    s = 0
                else:
                    i += 1
            if s != 0:
                day += 1
            return day <= days
        
        l = max(weights)
        h = sum(weights)
        if days == 1:
            return h
        ans = float("inf")
        while l <= h:
            mid = (l + h) //2
            if func(mid):
                ans = min(ans, mid)
                h = mid - 1
            else:
                l = mid + 1
        
        return ans
