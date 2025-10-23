from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(x for x in s)
        t_list = list(x for x in t)
        s_list.sort()
        t_list.sort()
        return s_list == t_list

    def isAnagram_v_2(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    def isAnagram_v_3(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1

        return True