class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ''' BRUTE FORCE'''
        for i in range(len(nums)):
            for j in range(len(nums)):
                #print(i,j,"indexes")
                #print(nums[i],nums[j],"values")
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]
        return 0