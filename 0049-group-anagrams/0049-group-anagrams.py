class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = defaultdict(list)

        for i in strs:
            arr[''.join(sorted(i))].append(i)
        
        return list(arr.values())

