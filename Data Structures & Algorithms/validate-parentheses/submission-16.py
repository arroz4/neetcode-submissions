class Solution:
    def isValid(self, s: str) -> bool:
        check = { ")":"(", "}":"{", "]":"["}
        seen = []

        for char in s:
            if char in "{[(":
                seen.append(char)
            elif char in check:
                if seen and check[char] == seen[-1]:
                    seen.pop()
                else:
                    return False
        return len(seen) == 0