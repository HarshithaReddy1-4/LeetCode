class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, j in enumerate(nums):
            s = 0
            while j > 0:
                p = j % 10
                s += p
                j //= 10
            if s == i:
                return i
        return -1
            