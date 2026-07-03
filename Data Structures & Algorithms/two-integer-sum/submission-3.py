class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for index,value in enumerate(nums):
            second_value=target-value
            if second_value in hashmap:
                return [hashmap[second_value],index]
            hashmap[value]=index
        return