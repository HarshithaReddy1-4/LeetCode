class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        i = 0
        while i < len(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            l = i + 1
            h = len(nums ) - 1
            m = nums[i]
            target = -m
            while l < h:
                if nums[l] + nums[h] == target:
                    res.append([m, nums[l], nums[h]])
                    l += 1
                    h -= 1
                    while l < h and nums[l] == nums[l - 1]:
                        l += 1
                    while l < h and nums[h] == nums[h + 1]:
                        h -= 1
                elif nums[l] + nums[h] > target:
                    h -= 1
                else:
                    l += 1
            i += 1
        return res
