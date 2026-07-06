class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        n = len(name)
        m = len(typed)
        while i < n and j < m:
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif i > 0 and name[i - 1] == typed[j]:
                j += 1
            else:
                return False
        if i != n:
            return False
        if j < m and ''.join(set(typed[j:])) != name[-1]:
            return False
        # while j < m:
        #     if typed[j] != name[-1]:
        #         return False
        #     j += 1
        return True
