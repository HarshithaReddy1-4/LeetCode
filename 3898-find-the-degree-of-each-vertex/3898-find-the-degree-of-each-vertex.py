class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        d = defaultdict(int)

        for i, j in enumerate(matrix):
            for num in j:
                if num:
                    d[i] += 1
            d[i]
        
        return list(d.values())