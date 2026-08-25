class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                max_val = max(max_val,arr[j])
            arr[i]=max_val
            max_val=-1
        return arr
