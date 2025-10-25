class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        pref = 1
        for i in range(len(nums)):
            res[i] = pref
            pref *= nums[i]
        postf = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postf
            postf *= nums[i]
        return res

    def productExceptSelf_v_2(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        return answer