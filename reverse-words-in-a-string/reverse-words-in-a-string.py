class Solution:
    def reverseWords(self, s: str) -> str:
        
        characters=s.split()
        return ' '.join(characters[::-1])
        