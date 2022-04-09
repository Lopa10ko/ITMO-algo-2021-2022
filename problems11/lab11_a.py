from sys import setrecursionlimit
import threading
from heapq import heappop, heappush
setrecursionlimit(10 ** 9)
threading.stack_size(3 * 67108864)

def main():
    #Dijkstra algo
    def dijkstra(graph, start_vertex, finish_vertex):
        my_heap = []
        weight_map = {w: float("inf") for w in graph.keys()}
        weight_map[start_vertex] = 0
        heappush(my_heap, (0, start_vertex))
        while my_heap:
            weight, vertex = heappop(my_heap)
            for vertex1, cur_weight in graph[vertex]:
                temp_weight = weight + cur_weight
                if temp_weight < weight_map[vertex1]:
                    weight_map[vertex1] = temp_weight
                    heappush(my_heap, (temp_weight, vertex1))
        return weight_map[finish_vertex] if weight_map[finish_vertex] != float("inf") else -1

    file_input, file_output = open('pathmgep.in', 'r'), open('pathmgep.out', 'w')
    N, S, F = map(int, file_input.readline().split())
    matrix = {}
    for i in range(N):
        current = list(map(int, file_input.readline().split()))
        concurrent = []
        for j in range(N):
            if i != j and current[j] != -1:
                concurrent.append((j, current[j]))
        matrix[i] = concurrent
        del concurrent
    print(dijkstra(matrix, S - 1, F - 1), file=file_output)
    file_output.close()

thread = threading.Thread(target=main)
thread.start()