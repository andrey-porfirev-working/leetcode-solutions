class ATM:

    def __init__(self):
        self.banknote_counts = [0, 0, 0, 0, 0]  # 20/50/100/200/500
        self.bnvalues = (20, 50, 100, 200, 500)
        self.num_denominations = len(self.banknote_counts)

    def deposit(self, banknotesCount: list[int]) -> None:
        for i in range(len(banknotesCount)):
            if banknotesCount[i] > 0:
                self.banknote_counts[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> list[int]:
        withdrawal_counts = [0, 0, 0, 0, 0]
        for i in reversed(range(self.num_denominations)):
            notes_to_use = min(amount // self.bnvalues[i], self.banknote_counts[i])
            withdrawal_counts[i] = notes_to_use
            amount -= notes_to_use * self.bnvalues[i]
        if amount > 0:
            return [-1]
        for i, count in enumerate(withdrawal_counts):
            self.banknote_counts[i] -= count
        return withdrawal_counts