class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxx = []
        minn = [-1] * n
        maxvar = float("-inf")
        for i in nums:
            maxvar = max(maxvar, i)
            maxx.append(maxvar)
        
        minvar = float("inf")
        for i in range(n - 1, -1, -1):
            minvar = min(minvar, nums[i])
            minn[i] = minvar

        idx = float("inf")
        c = 0
        for i, j in zip(maxx, minn):
            if i - j <= k:
                idx = min(idx, c)
            c += 1

        return idx if idx != float("inf") else -1
        