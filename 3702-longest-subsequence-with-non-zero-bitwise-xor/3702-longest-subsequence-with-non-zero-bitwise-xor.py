class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0
        n = len(nums)

        for i in nums:
            xor ^= i
        
        if xor == 0:
            ss = set(nums)
            if len(ss) == 1 and nums[0] == 0:
                return 0
            return n - 1
        
        return n