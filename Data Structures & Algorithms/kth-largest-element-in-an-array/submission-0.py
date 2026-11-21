class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for num in nums:
            if len(heap) == k:
                heapq.heappush(heap, num)
                heapq.heappop(heap)
            else:
                heapq.heappush(heap, num)

        return heap[0]

        