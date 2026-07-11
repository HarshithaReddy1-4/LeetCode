class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax, rightmax = 0, 0
        left, right = 0, len(height) - 1
        water = 0
        while left < right:
            if height[left] < height[right]:
                if leftmax > height[left]:
                    water += leftmax - height[left]
                else:
                    leftmax = height[left]
                left += 1
            else:
                if rightmax > height[right]:
                    water += rightmax - height[right]
                else:
                    rightmax = height[right]
                right -= 1
        return water