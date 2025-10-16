class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        return set(nums) <= k

#Test Cases
cases = [[1,2,3,1], [1,2,3,4],[1,1,1,3,3,4,3,2,4,2]]
correct_results = [True, False, True]
test = Solution_2()
for i in range(len(cases)):
    solution_result = test.containsDuplicate(cases[i])
    solution_correct_result = correct_results[i]
    print(f"Тест номер {i+1}")
    print(f"Входные данные: {cases[i]}\nРезультат работы: {solution_result}"
          f"\nОжидаемый результат: {solution_correct_result}")
    if solution_result != solution_correct_result:
        print("НЕСООТВЕТСТВИЕ РЕЗУЛЬТАТАМ!!!")
    else:
        print(">>>>>>>>>>Тест прошел!")