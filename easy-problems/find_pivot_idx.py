class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sum_right = sum(nums)
        sum_left = 0
        for i in range(len(nums)):
            sum_right -= nums[i]
            if sum_left == sum_right:
                return i
            sum_left += nums[i]
        return -1

    def pivotIndex_v_2(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            # Правая сумма = общая сумма - левая сумма - текущий элемент
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]

        return -1