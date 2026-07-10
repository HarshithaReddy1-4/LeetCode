class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def func(i, l):
            if len(l) == k:
                res.append(l)
                return
            if i > n:
                return
            func(i + 1, l + [i])
            func(i + 1, l)
        func(1, [])
        return res