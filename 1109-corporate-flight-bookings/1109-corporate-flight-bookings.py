class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 2)
        for i, j, k in bookings:
            diff[i] += k
            diff[j + 1] -= k
        a = []
        s = 0
        for i in diff[1:-1]:
            s += i
            a.append(s)
        
        return a
            