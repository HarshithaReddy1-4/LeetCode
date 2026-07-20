class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        adj = {node: [] for node in range(n)}
        for i, j in richer:
            adj[j].append(i)

        quietAdj = {node: 0 for node in range(n)}
        for i, j in enumerate(quiet):
            quietAdj[j] = i

        ans = [0] * n

        @cache
        def dfs(i):
            res = quiet[i]
            if not adj[i]:
                return quiet[i]
            for node in adj[i]:
                res = min(dfs(node), res)
            return res
        
        for i in range(n):
            ans[i] = quietAdj[dfs(i)]
        
        return ans
        