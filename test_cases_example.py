#Test Cases
cases = []
correct_results = [] #be sure that cases and correct_results match with each others
test = Solution()
for i in range(len(cases)):
    solution_result = test.threeSum(cases[i]) #your method solution
    solution_correct_result = correct_results[i]
    print(f"Test Number {i+1}")
    print(f"Input Data: {cases[i]}\nResult: {solution_result}"
          f"\nExpected Result: {solution_correct_result}")
    if solution_result != solution_correct_result:
        print("WRONG!!!")
    else:
        print(">>>>>>>>>>Test is passed!!!")