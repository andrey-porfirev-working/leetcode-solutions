class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l_idx = 0
        r_idx = k-1
        sum_num = 0
        for i in range(k):
            sum_num += nums[i]
        max_avrg = sum_num / k
        while r_idx < len(nums):
            sum_num -= nums[l_idx]
            l_idx += 1
            r_idx += 1
            if r_idx == len(nums):
                break
            sum_num += nums[r_idx]
            new_avrg = sum_num / k
            if max_avrg < new_avrg:
                max_avrg = new_avrg
        return max_avrg

    def findMaxAverage_v_2(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum = current_sum
        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, current_sum)
        return max_sum / k