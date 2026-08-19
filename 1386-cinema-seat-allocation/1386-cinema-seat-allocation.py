class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = [[1, 2, 3, 4], [3, 4, 5, 6], [5, 6, 7, 8]]
        rows = list(set([i - 1 for i, j in reservedSeats]))
        d = defaultdict(list)
        for i, j in reservedSeats:
            d[i - 1].append(j - 1)
        
        count = (n - len(rows)) * 2
        for i in rows:
            nums = [0] * 10
            for i1 in d[i]:
                nums[i1] = 1
            for j1, j2, j3, j4 in seats:
                if nums[j1] == 0 and nums[j2] == 0 and nums[j3] == 0 and nums[j4] == 0:
                    nums[j1], nums[j2], nums[j3], nums[j4] = 1, 1, 1, 1
                    count += 1

        return count
