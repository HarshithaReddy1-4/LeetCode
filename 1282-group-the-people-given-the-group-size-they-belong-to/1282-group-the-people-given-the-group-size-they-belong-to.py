class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        res = []
        n = len(groupSizes)

        for i in range(n):
            d[groupSizes[i]].append(i)
            if len(d[groupSizes[i]]) == groupSizes[i]:
                res.append(d[groupSizes[i]])
                d[groupSizes[i]] = []
        
        return res