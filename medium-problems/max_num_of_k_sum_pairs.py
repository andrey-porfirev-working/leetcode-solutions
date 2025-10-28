class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        res = 0

        nums.sort()
        while left < right:
            if nums[left] + nums[right] == k:
                res += 1
                del nums[right]
                del nums[left]
                right -= 2
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1
        return res

    def maxOperations_v_2(self, nums: list[int], k: int) -> int:
        freq = {}
        operations = 0

        for num in nums:
            complement = k - num

            if freq.get(complement, 0) > 0:
                operations += 1
                freq[complement] -= 1
            else:
                freq[num] = freq.get(num, 0) + 1

        return operations

test = Solution()
print(test.maxOperations([1,2,3,4], 5))