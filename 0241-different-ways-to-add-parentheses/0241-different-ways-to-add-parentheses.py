class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def func(exp):
            res = []
            for i in range(len(exp)):
                if exp[i] in '+-*':
                    left = func(exp[: i])
                    right = func(exp[i + 1:])
                    for x in left:
                        for y in right:
                            if exp[i] == '+':
                                res.append(x + y)
                            elif exp[i] == '-':
                                res.append(x - y)
                            elif exp[i] == '*':
                                res.append(x * y)
            if not res:
                res.append(int(exp))
            return res
        return func(expression)