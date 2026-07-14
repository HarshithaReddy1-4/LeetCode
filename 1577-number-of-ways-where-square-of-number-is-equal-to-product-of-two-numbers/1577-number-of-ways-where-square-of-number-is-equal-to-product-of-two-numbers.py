class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def count(a, b):
            ans = 0
            for i in a:
                target = i * i
                d = Counter()
                for j in b:
                    if target % j == 0:
                        ans += d[target // j]
                    d[j] += 1
            return ans
        return count(nums1, nums2) + count(nums2, nums1)
