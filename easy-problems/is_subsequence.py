class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        pointer_s, pointer_t = 0, 0
        while pointer_t < len(t):
            while s[pointer_s] != t[pointer_t]:
                pointer_t += 1
                if pointer_t == len(t):
                    return False
            pointer_s += 1
            pointer_t += 1
            if pointer_s == len(s):
                return True
        return False