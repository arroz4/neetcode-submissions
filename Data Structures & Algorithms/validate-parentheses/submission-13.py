class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets to their corresponding opening brackets
        bracket_map = {")": "(", "]": "[", "}": "{"}
        stack = []
        
        for char in s:
            if char not in bracket_map:
                # It's an opening bracket, push to stack
                stack.append(char)
            else:
                # It's a closing bracket
                # Check: stack must not be empty AND top must match
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
        
        # Valid only if all brackets are matched (stack is empty)
        return len(stack) == 0     