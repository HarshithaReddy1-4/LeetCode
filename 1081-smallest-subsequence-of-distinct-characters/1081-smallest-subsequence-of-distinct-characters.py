class Solution:
    def smallestSubsequence(self, s: str) -> str:
        lastOcc = {c: i for i, c in enumerate(s)}

        stack = []
        seen = set()

        for i, c in enumerate(s):
            if c in seen:
                continue
            
            while stack and c < stack[-1] and i < lastOcc[stack[-1]]:
                seen.remove(stack.pop())
            
            stack.append(c)
            seen.add(c)
        
        return ''.join(stack)