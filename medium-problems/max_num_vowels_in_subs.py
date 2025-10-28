class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        curr_values, max_values = 0, 0
        left, right = 0, -1
        while right < len(s)-1:
            right += 1
            if s[right] in vowels:
                curr_values += 1
            if right - left == k:
                if s[left] in vowels:
                    curr_values -= 1
                left += 1
            if curr_values == k:
                return curr_values
            max_values = max(curr_values, max_values)
        return max_values

    def maxVowels_v_2(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        current_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1

        max_vowels = current_vowels

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                current_vowels -= 1

            if s[i] in vowels:
                current_vowels += 1

            max_vowels = max(max_vowels, current_vowels)

        return max_vowels