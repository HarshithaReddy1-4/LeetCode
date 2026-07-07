class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        s = 0
        size = float('inf')

        for j in range(len(nums)):
            s += nums[j]
            while s >= target:
                size = min(size, j - i + 1)
                s -= nums[i]
                i += 1
        return size if size != float('inf') else 0
        