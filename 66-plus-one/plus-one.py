class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n=len(digits)
        carry=0
        for i in range(n-1,-1,-1):
            digits[i]+=1
            if digits[i]==10:
                digits[i]=0
                carry=1
            if digits[i]!=0:
                return digits
        if carry==1:
            digits.insert(0,1)
        return digits
            

