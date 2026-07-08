class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        curr = 0
        ans = 0

        for i in nums:
            curr += i

            if curr - k in prefix:
                ans += prefix[curr - k]
            
            prefix[curr] = prefix.get(curr, 0) + 1

        return ans