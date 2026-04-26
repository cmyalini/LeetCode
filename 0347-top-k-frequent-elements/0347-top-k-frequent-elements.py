class Solution(object):
    def topKFrequent(self, nums, k):
        from collections import Counter
        import heapq
        count = Counter(nums)
        return [item[0] for item in heapq.nlargest(k, count.items(),key=lambda x: x[1])]