class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxx = []
        maxvar = float("-inf")
        for i in nums:
            maxvar = max(maxvar, i)
            maxx.append(maxvar)
        
        minvar = float("inf")
        for i in range(n - 1, -1, -1):
            minvar = min(minvar, nums[i])
            maxx[i] = maxx[i] - minvar

        for i in range(n):
            if maxx[i] <= k:
                return i

        return -1
        