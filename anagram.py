class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s)==sorted(t):
            return True
        else:
            return False

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_m={}
        t_m={}
        for i in s:
            if i in s_m:
                s_m[i]=s_m[i]+1
            else:
                s_m[i]=1
            
        for j in t:
            if j in t_m:
                t_m[j]=t_m[j]+1
            else:
                t_m[j]=1
        return s_m==t_m
        
