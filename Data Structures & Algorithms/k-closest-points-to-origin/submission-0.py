class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        
        for x, y in points:
            # Use negative distance to simulate a max-heap
            distance = -(x**2 + y**2)
            
            heapq.heappush(max_heap, (distance, [x, y]))
            
            # Keep the heap size equal to k
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
        # Extract the coordinate points from the heap
        return [point for dist, point in max_heap]