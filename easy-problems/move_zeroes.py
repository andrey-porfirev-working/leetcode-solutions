class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                dummy = i+1
                while dummy < len(nums):
                    if nums[dummy] != 0:
                        nums[i] = nums[dummy]
                        nums[dummy] = 0
                        break
                    dummy += 1

    def moveZeroes_2(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write_ptr = 0
        for read_ptr in range(len(nums)):
            if nums[read_ptr] != 0:
                nums[write_ptr] = nums[read_ptr]
                write_ptr += 1
        for i in range(write_ptr, len(nums)):
            nums[i] = 0

test = Solution()
case = [0]
test.moveZeroes(case)
print(case)
