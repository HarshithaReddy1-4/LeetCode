class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = defaultdict(int)
        for i in nums2:
            while stack and stack[-1] < i:
                d[stack.pop()] = i
            stack.append(i)
            d[i] = -1
        
        ans = []
        for i in nums1:
            ans.append(d[i])

        return ans