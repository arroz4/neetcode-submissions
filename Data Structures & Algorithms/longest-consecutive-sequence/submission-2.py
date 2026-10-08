class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        items = sorted(set(nums))
        
        curCount = 1
        maxCount = 1
        for i in range(len(items)-1):
            if items[i+1]-items[i] == 1:
                curCount += 1
                maxCount = max(maxCount, curCount)
            else:
                curCount = 1
        return maxCount
