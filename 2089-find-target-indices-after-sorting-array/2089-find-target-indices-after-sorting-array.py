class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        first = sum(x < target for x in nums)
        count = sum(x == target for x in nums)

        return list(range(first, first + count))
