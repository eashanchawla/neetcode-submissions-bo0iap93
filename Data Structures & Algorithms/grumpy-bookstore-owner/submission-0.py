class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base_rec = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                base_rec += customers[i]
        max_rec = 0
        for i in range(len(grumpy) - minutes + 1):
            cust_rec = 0
            for j in range(i, i + minutes):
                if grumpy[j] == 1:
                    cust_rec += customers[j]
            max_rec = max(max_rec, cust_rec)
        return max_rec + base_rec