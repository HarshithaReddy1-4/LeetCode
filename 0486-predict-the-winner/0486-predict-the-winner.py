class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        @cache
        def func(i, j):
            if i == j:
                return nums[i]
            
            left = nums[i] - func(i + 1, j)
            right = nums[j] - func(i, j - 1)

            return max(left, right)
        
        return func(0, n - 1) >= 0