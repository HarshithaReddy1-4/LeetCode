class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if digits[n - 1] != 9:
            digits[n - 1] += 1
            return digits
        else:
            digits[n - 1] = 0
            for i in range(n - 2, -1, -1):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    return digits
            return [1] + digits
            