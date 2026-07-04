class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            count = [0]*26
            ## Uses array as key for hashmap
            for c in string:
                count[ord(c) - ord("a")] +=1
            #print(string,count)
            result[tuple(count)].append(string)
        return list(result.values())