class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def count(A, B):
            product = Counter()

            for i in range(len(B)):
                for j in range(i + 1, len(B)):
                    product[B[i] * B[j]] += 1
            ans = 0
            for x in A:
                ans += product[x * x]
            return ans

        return count(nums1, nums2) + count(nums2, nums1)
