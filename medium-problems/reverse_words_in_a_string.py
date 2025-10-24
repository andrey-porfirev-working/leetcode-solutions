class Solution:
    def reverseWords(self, s: str) -> str:
        words = list(filter(lambda x: x != "", s.split(" ")))
        return " ".join(words[::-1])


#Test Cases
cases = ["the sky is blue", "  hello world  ", "a good   example"]
correct_results = ["blue is sky the", "world hello", "example good a"] #be sure that cases and correct_results match with each others
test = Solution()
for i in range(len(cases)):
    solution_result = test.reverseWords(cases[i]) #your method solution
    solution_correct_result = correct_results[i]
    print(f"Test Number {i+1}")
    print(f"Input Data: {cases[i]}\nResult: {solution_result}"
          f"\nExpected Result: {solution_correct_result}")
    if solution_result != solution_correct_result:
        print("WRONG!!!")
    else:
        print(">>>>>>>>>>Test is passed!!!")

s = "   hello aboha   "
words = s.split(" ")
print(words)