class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string))+ "#"+string
        return result
        
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
        while i < len(s):
            j = i
            # Find the '#' delimiter
            while s[j] != "#":
                j += 1
            
            # Parse the length
            length = int(s[i:j])
            i = j + 1  # Move past '#'
            
            # Extract exactly 'length' characters (no matter what they are)
            result.append(s[i:i+length])
            i += length
        
        return result