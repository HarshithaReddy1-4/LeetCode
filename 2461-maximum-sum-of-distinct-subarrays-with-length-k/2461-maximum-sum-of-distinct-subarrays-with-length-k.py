class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxx = 0
        i = 0
        d = {}
        s = 0
        for j in range(len(nums)):
            d[nums[j]] = d.get(nums[j], 0) + 1
            s += nums[j]
            if j - i + 1 == k:
                if len(d) == k:
                    maxx = max(maxx, s)
                s -= nums[i]
                if nums[i] in d:
                    d[nums[i]] -= 1
                    if d[nums[i]] == 0:
                        del d[nums[i]]
                i += 1
        return maxx
            

