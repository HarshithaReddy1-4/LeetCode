class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)

        i = 0
        ans =float("-inf")

        for j in range(len(nums)):
            d[nums[j]] += 1
            while d[nums[j]] > k:
                d[nums[i]] -= 1
                i += 1
            
            ans = max(ans, j - i + 1)

        return ans
