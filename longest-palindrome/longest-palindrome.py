class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=defaultdict(int)
        odd=0
        total=0
        for i in range(len(s)):
            count[s[i]]+=1
            if count[s[i]]==2:
                count[s[i]]=0
                total+=2
                odd-=1
            else:
                odd+=1
        if odd>0:
            return total+1
        return total
                
            
            
                
        