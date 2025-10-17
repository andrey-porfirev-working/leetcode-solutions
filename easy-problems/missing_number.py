class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        dummy_set = set(range(n + 1))
        diff = dummy_set - set(nums)
        return diff.pop()

class Solution_2:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = n * (n + 1) // 2
        return total_sum - sum(nums)

