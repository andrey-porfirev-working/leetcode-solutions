import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = re.sub(r'[^a-zA-Z0-9]', "", s)
        print(clean_text)
        potential_palindrome = clean_text.lower()
        return potential_palindrome == potential_palindrome[::-1]

#Test Cases
cases = ["A man, a plan, a canal: Panama", "race a car", " ", "ab_a"]
correct_results = [True, False, True, True]
test = Solution()
for i in range(len(cases)):
    solution_result = test.isPalindrome(cases[i])
    solution_correct_result = correct_results[i]
    print(f"Тест номер {i+1}")
    print(f"Входные данные: {cases[i]}\nРезультат работы: {solution_result}"
          f"\nОжидаемый результат: {solution_correct_result}")
    if solution_result != solution_correct_result:
        print("НЕСООТВЕТСТВИЕ РЕЗУЛЬТАТАМ!!!")
    else:
        print(">>>>>>>>>>Тест прошел!")