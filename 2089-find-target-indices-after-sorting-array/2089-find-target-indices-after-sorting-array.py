class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        n = len(nums) - 1
        l, h = 0, n
        ans = []
        first = -1
        last = -1

        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                first = mid
                h = mid - 1
            elif nums[mid] > target:
                h = mid - 1
            else:
                l = mid + 1
        
        l = 0
        h = n
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                last = mid
                l = mid + 1
            elif nums[mid] > target:
                h = mid - 1
            else:
                l = mid + 1

        if first == -1:
            return [] 
            
        for i in range(first, last + 1):
            ans.append(i)
        
        return ans
