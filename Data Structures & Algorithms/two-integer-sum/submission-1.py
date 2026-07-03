class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            first_number = nums[i]
            second_number= target-first_number
            if second_number in nums:
                j = nums.index(second_number)
                if i != j:
                    result = [i, j]
                    result.sort()
                    return result
        
        return result
