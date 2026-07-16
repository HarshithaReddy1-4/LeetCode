class Solution(object):
    def generate(self, numRows):
        # if numRows == 0:
        #     return []
        # elif numRows == 1:
        #     return [[1]]
        # elif numRows == 2:
        #     return [[1], [1,1]]
        # res = [[1], [1, 1]]
        # for i in range(1, numRows - 1):
        #     t = [1]
        #     for j in range(len(res[i]) - 1):
        #         t.append(res[i][j] + res[i][j + 1])
        #     t.append(1)
        #     res.append(t)
        # return res

        dp = [[1] * (i + 1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        return dp
        