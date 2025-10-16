# Solutuon_1: runtime - 10ms (79.21 % beaten), memory - 31.55 mb (53.75 % beaten)
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
# Solutuon_2: runtime - 16ms (44.40 % beaten), memory - 31.56 mb (53.75 % beaten)
class Solution_2:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

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


