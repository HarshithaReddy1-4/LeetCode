class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr2 = sorted(set(arr))
        res = []
        d = {}
        for i, j in enumerate(arr2):
            d[j] = i + 1
        for i in arr:
            res.append(d[i])
        return res
