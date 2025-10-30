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

    def decodeString_v_2(self, s: str) -> str:
        nums = [""]
        words = [""]

        for char in s:
            if char.isdigit():
                nums[-1] += char
            elif char == "[":
                nums[-1] = int(nums[-1])
                nums.append("")
                words.append("")
            elif char == "]":
                num = nums.pop(-2)
                current_word = words.pop()
                words[-1] += current_word * num
            else:
                words[-1] += char

        return words[0]