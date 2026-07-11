class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        h = len(numbers) - 1
        while l <= h:
            m = numbers[l] + numbers[h]
            if m == target:
                return [l+  1, h + 1]
            if m > target:
                h -= 1
            else:
                l += 1

        
