class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        i=0
        result=[]
        while len(strs) > 0:
            reference_word = strs.pop(0)
            new_collection = [reference_word]

            j = 0
            while j < len(strs):
                if "".join(sorted(strs[j]))== "".join(sorted(reference_word)):
                    new_collection.append(strs.pop(j))
                else:
                    j+=1
            result.append(new_collection)
        return result