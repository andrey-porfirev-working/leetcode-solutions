from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        c_arr = Counter(arr)
        return len(c_arr) == len(set(c_arr.values()))