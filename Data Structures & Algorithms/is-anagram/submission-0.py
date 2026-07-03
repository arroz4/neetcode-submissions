class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        counter2={}

        for letter in s:
            if letter in counter.keys():
                counter[letter] += 1
            else:
                counter[letter] = 1
        
        for letter in t:
            if letter in counter2.keys():
                counter2[letter] += 1
            else:
                counter2[letter] = 1
        
        if counter == counter2:
            return True
        else:
            return False