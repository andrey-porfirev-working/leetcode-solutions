class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        results = []
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                if start == nums[i - 1]:
                    results.append(str(start))
                else:
                    results.append(f"{start}->{nums[i - 1]}")
                start = nums[i]
        if start == nums[-1]:
            results.append(str(start))
        else:
            results.append(f"{start}->{nums[-1]}")
        return results

#Test Cases
cases = [[0,1,2,4,5,7], [0,2,3,4,6,8,9]]
correct_results = [["0->2","4->5","7"],["0","2->4","6","8->9"]]
test = Solution()
for i in range(len(cases)):
    solution_result = test.summaryRanges(cases[i])
    solution_correct_result = correct_results[i]
    print(f"Тест номер {i+1}")
    print(f"Входные данные: {cases[i]}\nРезультат работы: {solution_result}"
          f"\nОжидаемый результат: {solution_correct_result}")
    if solution_result != solution_correct_result:
        print("НЕСООТВЕТСТВИЕ РЕЗУЛЬТАТАМ!!!")
    else:
        print(">>>>>>>>>>Тест прошел!")