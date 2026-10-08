class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        for n in nums:
            res[n] = res.get(n,0) +1
        return sorted(res.items(), key=lambda x: x[1])[-1][0]