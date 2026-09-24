class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t) : return False

        seen = [0]*26

        for char in s:
            seen[ord(char)-97]+=1
        
        for char in t:
            seen[ord(char)-97]-=1
        
        for i in range(len(seen)):
            if seen[i]!=0:
                return False
                
        return True
        
