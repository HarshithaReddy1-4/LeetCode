class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        n = len(nums)
        def func(i, s):
            if i >= n:
                if s == target:
                    return 1
                return 0
            
            if (i, s) in memo:
                return memo[(i, s)]
            
            memo[(i, s)] = (func(i + 1, s + nums[i]) + func(i + 1, s - nums[i]))
            return memo[(i, s)]
        
        return func(0, 0)
