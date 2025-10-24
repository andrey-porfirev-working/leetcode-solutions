class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        s = list(l for l in s)
        vowel_1 = ""
        vowel_2 = ""
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] in vowels:
                vowel_1 = s[left]
            else:
                left += 1
            if s[right] in vowels:
                vowel_2 = s[right]
            else:
                right -= 1
            if vowel_1 and vowel_2:
                s[left] = vowel_2
                s[right] = vowel_1
                vowel_1 = ""
                vowel_2 = ""
                left += 1
                right -= 1
        result = ""
        for l in s:
            result += l
        return result