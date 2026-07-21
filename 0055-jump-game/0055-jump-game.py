class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        curr = nums[0]
        for i in range(1, n):
            if curr - 1 < 0:
                return False
            curr = max(nums[i], curr - 1)
        return True