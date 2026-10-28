class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for s in strs:
            if str(sorted(s)) in groups:
                groups[str(sorted(s))].append(s)
            else:
                groups[str(sorted(s))] = [s]
        return [y for x,y in groups.items()]