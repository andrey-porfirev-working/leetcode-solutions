class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        match_s_to_t = dict()
        match_t_to_s = dict()
        for i in range(len(s)):
            if s[i] not in match_s_to_t:
                match_s_to_t[s[i]] = t[i]
            if match_s_to_t[s[i]] != t[i]:
                return False
            if t[i] not in match_t_to_s:
                match_t_to_s[t[i]] = s[i]
            if match_t_to_s[t[i]] != s[i]:
                return False
        return True

    def isIsomorphic_v_2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return (len(set(zip(s, t))) == len(set(s)) == len(set(t)))