from sys import setrecursionlimit
import array
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(3 * 67108864)
 
def main():
    #Dijkstra algo
    file_input, file_output = open('pathmgep.in', 'r'), open('pathmgep.out','w')
    N, start_vertex, finish_vertex = map(int, file_input.readline().split())
    matrix = [list(map(float, file_input.readline().replace("-1", "inf").split())) for _ in range(N)]
    weight_map, marked = [float("inf")] * N, array.array('b', [0] * N)
    weight_map[start_vertex - 1] = 0 # (a,a)
    #full matrix O(n^2) iteration
    for _ in range(N):
        current_vertex_weight = float("inf")
        current_vertex = None
        #find min_weight vertex
        for i in range(N):
            if not marked[i]:
                if weight_map[i] < current_vertex_weight:
                    current_vertex = i
                    current_vertex_weight = weight_map[i]
        if current_vertex_weight == float("inf"): break
        for i in range(N):
            weight_map[i] = min(weight_map[i], weight_map[current_vertex] + matrix[current_vertex][i])
        marked[current_vertex] = 1
    #if finish -> inf, path does not exist
    print(-1 if weight_map[finish_vertex - 1] == float("inf") else int(weight_map[finish_vertex - 1]), file=file_output)
    file_output.close()
 
thread = threading.Thread(target=main)
thread.start()