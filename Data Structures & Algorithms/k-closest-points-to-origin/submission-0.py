import heapq   
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        for lista in points:
            if len(heap) == k:
                heapq.heappush(heap,(-(lista[0]**2 + lista[1]**2),[lista[0],lista[1]]))
                heapq.heappop(heap)
            else:
                heapq.heappush(heap,(-(lista[0]**2 + lista[1]**2),[lista[0],lista[1]]))

        result = []
        for _ in range(k):

            module, coordenades = heapq.heappop(heap)
            result.append(coordenades)
        
        return result






        