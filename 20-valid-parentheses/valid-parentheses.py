class Solution:
    def isValid(self, s: str) -> bool:
        stack = []*len(s)
        top = -1
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
                top+=1

            else:
                if len(stack)==0:
                    return False

                if stack[top] == '(' and s[i] == ')' or stack[top] == '{' and s[i] == '}' or stack[top] == '[' and s[i] == ']':
                    stack.pop()
                    top-=1
                else:
                    return False
        return len(stack)==0