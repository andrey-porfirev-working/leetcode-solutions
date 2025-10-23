class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        length_first = len(word1)
        length_second = len(word2)
        first_pointer = 0
        second_pointer = 0
        while first_pointer != length_first or second_pointer != length_second:
            if first_pointer < length_first:
                result += word1[first_pointer]
                first_pointer += 1
            if second_pointer < length_second:
                result += word2[second_pointer]
                second_pointer += 1
        return result

    def mergeAlternately_v_2(self, word1: str, word2: str) -> str:
        result = []
        for a, b in zip(word1, word2):
            result.append(a)
            result.append(b)
        result.append(word1[len(word2):])
        result.append(word2[len(word1):])
        return ''.join(result)