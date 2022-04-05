from sys import setrecursionlimit
import threading
from heapq import *
setrecursionlimit(10 ** 9)
threading.stack_size(3 * 67108864)
 
def main():
    #Dijkstra algo heapify O(mlogn)
    file_input, file_output = open('pathbgep.in', 'r'), open('pathbgep.out','w')
    n, m = map(int, file_input.readline().split())
    matrix = [{} for _ in range(n)]
    for _ in range(m):
        current = list(map(int, file_input.readline().split()))
        matrix[current[0] - 1][current[1] - 1] = current[2]
        matrix[current[1] - 1][current[0] - 1] = current[2]
    #heap vertexi: {vertexj, weight}
    # print(matrix)
    my_heap = [(0, 0)]
    marked, weight_map = [0] * n, [None] * n
    while my_heap:
        weight, vertex = heappop(my_heap)
        if weight_map[vertex] is None:
            weight_map[vertex] = weight
            for vertex1 in matrix[vertex]:
                if weight_map[vertex1] is None:
                    heappush(my_heap, (matrix[vertex][vertex1] + weight, vertex1))
    print(*weight_map, file=file_output)
    file_output.close()

thread = threading.Thread(target=main)
thread.start()