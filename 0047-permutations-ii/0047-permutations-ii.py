class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def func(op, ip):
            if len(ip) == 0:
                if op not in res:
                    res.append(op)
                return
            for i in range(len(ip)):
                func(op + [ip[i]], ip[:i] + ip[i + 1:])
        func([], nums)
        return res

