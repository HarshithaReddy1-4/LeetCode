class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        setA, setB = set(), set()
        ans = []
        count = 0

        for i, j in zip(A, B):
            setA.add(i)
            setB.add(j)
            if i == j:
                count += 1
            else:
                if i in setB:
                    count += 1
                if j in setA:
                    count += 1
            ans.append(count)
        return ans