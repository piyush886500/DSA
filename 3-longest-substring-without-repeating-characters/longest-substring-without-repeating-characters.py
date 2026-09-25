class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        longest=0
        unique = set()
        for i in range(len(s)):
            while s[i] in unique:
                unique.remove(s[l])
                l+=1
            w = (i-l)+1
            longest = max(w,longest)
            unique.add(s[i])
        return longest
            
