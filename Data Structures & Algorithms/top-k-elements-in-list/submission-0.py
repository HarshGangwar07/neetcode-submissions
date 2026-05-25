class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            dict[num] = dict.get(num,0) + 1
        return heapq.nlargest(k , dict , key=dict.get)
        