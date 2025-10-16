class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

#testcases
test = Solution()
print(test.singleNumber([2,2,1])) #must be 1
print(test.singleNumber([4,1,2,1,2])) #must be 4
print(test.singleNumber([1])) #must be 1