class Solution:
    def twoSum(self, nums, target):
        d = {num: i for i, num in enumerate(nums)}
        for i in range(len(nums)):
            j = target - nums[i]
            if j in d and i != d[j]:
                return [i, d[j]]