class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        n = len(prices)
        ans = prices[:]

        for i in range(n):
            while stack and stack[-1][0] >= prices[i]:
                p, idx = stack.pop()
                ans[idx] = p - prices[i]
            stack.append([prices[i], i])
        
        return ans
                