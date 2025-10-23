class Solution:
    def hasSameDigits(self, s: str) -> bool:
        nums = list(map(int,s))
        while len(nums) > 2:
            for i in range(len(nums)-1):
                nums[i] = (nums[i]+nums[i+1])%10
            del nums[-1]
        return nums[0] == nums[1]
    def hasSameDigits_v_2(self, s: str) -> bool:
        digits = list(map(int, s))
        while len(digits) > 2:
            new_digits = []
            for i in range(len(digits) - 1):
                new_digits.append((digits[i] + digits[i+1]) % 10)
            digits = new_digits
        return digits[0] == digits[1]

#Test Cases
cases = ["3902", "34789"]
correct_results = [True, False] #be sure that cases and correct_results match with each others
test = Solution()
for i in range(len(cases)):
    solution_result = test.hasSameDigits(cases[i]) #your method solution
    solution_correct_result = correct_results[i]
    print(f"Test Number {i+1}")
    print(f"Input Data: {cases[i]}\nResult: {solution_result}"
          f"\nExpected Result: {solution_correct_result}")
    if solution_result != solution_correct_result:
        print("WRONG!!!")
    else:
        print(">>>>>>>>>>Test is passed!!!")