class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for key, value in enumerate(nums):
            second_number = target-value
            if second_number in hashmap.keys():
                return [hashmap[second_number],key]
            
            hashmap[value] = key