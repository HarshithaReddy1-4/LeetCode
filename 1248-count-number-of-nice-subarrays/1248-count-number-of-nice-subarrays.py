class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atmost(n):
            if n < 0:
                return 0
            
            i = 0
            ans = 0

            for j in range(len(nums)):
                if nums[j] % 2:
                    n -= 1
                
                while n < 0:
                    if nums[i] % 2:
                        n += 1
                    i += 1
                ans += j - i + 1
            return ans
        
        return atmost(k) - atmost(k - 1)
                
