class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for key,value in enumerate(nums):
            first_number = target-value
            if first_number in seen: ## seen.keys() caused me error in edge case also
                return [seen[first_number],key]
            else:
                seen[value] = key ## .get method caused me error in edge case
        return False