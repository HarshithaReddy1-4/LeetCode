class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(k):
            if k < 0:
                return 0
            i = 0
            s = 0
            c = 0

            for j in range(len(nums)):
                s += nums[j]
                while s > k:
                    s -= nums[i]
                    i += 1
                c += (j - i + 1)
            
            return c

        return atMost(goal) - atMost(goal - 1)

        # pref = {0: 1}
        # s = 0
        # ans = 0
        # for i in range(len(nums)):
        #     s += nums[i]

        #     ans += pref.get(s - goal, 0)
            
        #     pref[s] = pref.get(s, 0) + 1
        
        # return ans
            