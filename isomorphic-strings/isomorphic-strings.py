class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        
        s_tMapping={}
        t_sMapping={}
        
        for i in range(len(s)):
            if s[i] in s_tMapping:
                if s_tMapping[s[i]]!=t[i]:
                    return False
            else:
                s_tMapping[s[i]]=t[i]
            
            if t[i] in t_sMapping:
                if t_sMapping[t[i]]!=s[i]:
                    return False
            else:
                t_sMapping[t[i]]=s[i]
        
        return True
        