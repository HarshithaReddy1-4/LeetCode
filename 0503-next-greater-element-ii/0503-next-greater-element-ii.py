class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ans = [-1] * n
        
        for _ in range(2):
            for i in range(n):
                while stack and stack[-1][0] < nums[i]:
                    num, idx = stack.pop()
                    ans[idx] = nums[i]
                stack.append([nums[i], i])

        return ans
        
