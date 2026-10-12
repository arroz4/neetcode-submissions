class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pali(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        L, R = 0, len(s) - 1

        while L < R:
            if s[L] == s[R]:
                L += 1
                R -= 1
            else:
                return is_pali(L + 1, R) or is_pali(L, R - 1)
        return True