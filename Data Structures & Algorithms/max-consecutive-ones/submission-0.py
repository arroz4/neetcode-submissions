class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count_one = 0
        max_count = 0
        for one in nums:
            if one == 1:
                count_one +=1
                max_count = max(max_count,count_one)
            else:
                count_one=0
        return max_count