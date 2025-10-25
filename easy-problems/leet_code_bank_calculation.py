class Solution:
    def totalMoney(self, n: int) -> int:
        new_week = 1
        to_add = new_week
        total = 0
        for d in range(1, n+1):
            total += to_add
            to_add += 1
            if d%7 == 0:
                new_week += 1
                to_add = new_week
        return total

    def totalMoney_v_2(self, n: int) -> int:
            weeks = n // 7
            days_left = n % 7

            total = (7 * weeks * (weeks + 1)) // 2 + 21 * weeks
            total += days_left * weeks + (days_left * (days_left + 1)) // 2

            return total