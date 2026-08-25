class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        ans = nums
        for item in range(0,len(nums)):
            ans.append(nums[item])
        return ans