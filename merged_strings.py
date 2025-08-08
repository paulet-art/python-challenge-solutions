class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_strings = ''.join(a+b for a,b in zip_longest(word1, word2,        fillvalue=''))
        return merged_strings
