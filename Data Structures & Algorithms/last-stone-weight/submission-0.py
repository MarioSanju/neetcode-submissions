import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = []
        for stone in stones:
            heap.append(-stone)

        heapq.heapify(heap)

        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x > y:
                heapq.heappush(heap, -(x - y))
        if heap:
            return -heap[0]
        return 0

        