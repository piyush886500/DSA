class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        seen = [False]*26

        for char in sentence:
            seen[ord(char) - 97] = True
        
        for check in seen:
            if check == False:
                return False
                
        return True