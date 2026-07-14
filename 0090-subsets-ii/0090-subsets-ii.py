class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def func(i, l):
            res.append(l[:])
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                l.append(nums[j])
                func(j + 1, l)
                l.pop()
            
        func(0, [])
        return res