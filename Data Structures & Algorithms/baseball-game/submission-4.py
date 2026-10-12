class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for item in operations:
            if item == '+':
                stack.append(stack[-1] + stack[-2])
            elif item == 'D':
                stack.append(stack[-1] * 2)
            elif item == 'C':
                stack.pop()
            else:
                stack.append(int(item))
        return sum(stack)