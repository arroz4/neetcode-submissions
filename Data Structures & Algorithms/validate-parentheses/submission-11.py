class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for item in s:
            ## openings
            if item in '([{':
                stack.append(item)
            else:
                if len(stack) == 0:
                    return False
                
                if stack[-1] == '(' and item == ')':
                    stack.pop()
                elif stack[-1] == '[' and item == ']':
                    stack.pop()
                elif stack[-1] == '{' and item == '}':
                    stack.pop()
                else:
                    return False

        return len(stack)==0
