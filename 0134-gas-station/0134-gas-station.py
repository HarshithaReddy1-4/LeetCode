class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        balance, defect, start = 0, 0, 0
        for i in range(len(gas)):
            balance += gas[i] - cost[i]
            if balance < 0:
                defect += balance
                balance = 0
                start = i + 1
        if defect + balance >= 0:
            return start
        return -1
        