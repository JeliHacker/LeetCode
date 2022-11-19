import heapq

def kClosest(points: list[list[int]], K: int) -> list[list[int]]:
        
        heap = []
        
        for (x, y) in points:
            dist = -(x*x + y*y)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [(x,y) for (dist,x, y) in heap]


input_points = [[1,3],[-2,2]]
input_k = 1
print(kClosest(input_points, input_k))
