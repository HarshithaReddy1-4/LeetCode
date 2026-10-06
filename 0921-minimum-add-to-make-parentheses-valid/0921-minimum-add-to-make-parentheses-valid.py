class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open, close = 0, 0

        for i in s:
            if i == '(':
                open += 1
            elif open > 0:
                open -= 1
            else:
                close += 1

        if open >  0 and close > 0:
            return open + close
        
        return abs(open - close)
