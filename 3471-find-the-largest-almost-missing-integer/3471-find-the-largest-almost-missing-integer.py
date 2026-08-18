class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k == n:
            return max(nums)
        
        d = Counter(nums)
        if k == 1:
            maxx = -1
            for k, v in d.items():
                if v == 1 and k > maxx:
                    maxx = k
            return maxx
        
        if d[nums[0]] == 1 and d[nums[n - 1]] == 1:
            return max(nums[0], nums[n - 1])

        if d[nums[0]] == 1:
            return nums[0]

        if d[nums[n - 1]] == 1:
            return nums[n - 1]
        
        return -1

            