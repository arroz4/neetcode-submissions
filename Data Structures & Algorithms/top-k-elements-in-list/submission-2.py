class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for num in nums:
            res[num] = res.get(num,0)+1
        sorted_items = sorted(res.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]