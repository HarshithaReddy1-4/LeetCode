class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        close = float("inf")
        summ = 0
        n = len(nums)
        for i in range(n):
            l = i + 1
            h = n - 1
            while l < h:
                m = nums[i] + nums[l] + nums[h]
                if m > target:
                    h -= 1
                elif m < target:
                    l += 1
                else:
                    return m
                if abs(target - m) < close:
                    close = abs(target - m)
                    summ = m
        return summ

