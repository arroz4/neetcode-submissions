class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for key,value in enumerate(nums):
            first_number = target-value
            if first_number in seen:
                return [seen[first_number],key]
            else:
                seen[value] = key