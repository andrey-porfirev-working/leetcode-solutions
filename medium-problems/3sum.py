class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        results = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return results

#Test Cases
cases = [[-1,0,1,2,-1,-4], [0,1,1],[0,0,0], [0,0,0,0], [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]]
correct_results = [[[-1,-1,2],[-1,0,1]], [], [[0,0,0]], [[0,0,0]], [[-10,5,5],[-5,0,5],[-4,2,2],[-3,-2,5],[-3,1,2],[-2,0,2]]]
test = Solution()
for i in range(len(cases)):
    solution_result = test.threeSum(cases[i])
    solution_correct_result = correct_results[i]
    print(f"Тест номер {i+1}")
    print(f"Входные данные: {cases[i]}\nРезультат работы: {solution_result}"
          f"\nОжидаемый результат: {solution_correct_result}")
    if solution_result != solution_correct_result:
        print("НЕСООТВЕТСТВИЕ РЕЗУЛЬТАТАМ!!!")
    else:
        print(">>>>>>>>>>Тест прошел!")
