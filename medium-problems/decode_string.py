class Solution:
    def decodeString(self, s: str) -> str:
        stack_of_nums = [""]
        stack_words_to_add = [""]
        res = ""
        for l in s:
            if l.isdigit():
                stack_of_nums[-1] += l
            elif l == "]":
                stack_words_to_add[-2] += stack_words_to_add[-1] * stack_of_nums[-2]
                stack_words_to_add.pop()
                stack_of_nums.pop(-2)
            elif l == "[":
                stack_of_nums[-1] = int(stack_of_nums[-1])
                stack_of_nums.append("")
                stack_words_to_add.append("")
            else:
                stack_words_to_add[-1] += l
        return stack_words_to_add[-1]