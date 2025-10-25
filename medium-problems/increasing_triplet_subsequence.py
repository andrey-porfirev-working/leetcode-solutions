class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(set(nums)) >= 3:
            for i in range(len(nums)-2):
                for j in range(i+1, len(nums)-1):
                    if nums[i] < nums[j]:
                        for k in range(j, len(nums)):
                            if nums[j] < nums[k]:
                                return True
        return False
    def increasingTriplet_v_2(self, nums: list[int]) -> bool:
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False