class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        base = strs[0]
        prefix = ""
        for i in range(len(base)):

            for item in strs[1:]:
                if i == len(item) or base[i] != item[i]:
                    return prefix
            prefix = prefix+base[i]
        return prefix

             