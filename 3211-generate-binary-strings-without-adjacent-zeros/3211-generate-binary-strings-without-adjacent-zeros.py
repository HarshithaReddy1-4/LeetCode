class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []

        def func(i, s, zero):
            if i == n:
                res.append(s)
                return
            if zero:
                func(i + 1, s + '1', False)
                return
            func(i + 1, s + '0', True)
            func(i + 1, s + '1', False)
            
        func(0, '', False)
        return res