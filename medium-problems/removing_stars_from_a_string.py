class Solution:
    def removeStars(self, s: str) -> str:
        pointer = 0
        res = ""

        while pointer < len(s):
            if s[pointer] == "*":
                res = res[:-1]
            else:
                res += s[pointer]
            pointer += 1

        return res

    def removeStars_v_2(self, s: str) -> str:
        res = ""

        for l in s:
            if l == "*":
                res = res[:-1]
            else:
                res += l

        return res

    def removeStars_v_3(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == '*':
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)