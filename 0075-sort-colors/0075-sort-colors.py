class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid = 0, 0
        n = len(nums)
        high = n - 1
        for i in range(n):
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid],  nums[high] = nums[high], nums[mid]
                high -= 1
            else:
                mid += 1
        