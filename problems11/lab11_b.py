from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(3 * 67108864)
 
def main():
    #Dijkstra algo
    file_input, file_output = open('pathsg.in', 'r'), open('pathsg.out','w')
    n, m = map(int, file_input.readline().split())
    matrix = [[float("inf")] * n for _ in range(n)]
    for iter in range(m):
        current = list(map(int, file_input.readline().split()))
        matrix[current[0] - 1][current[1] - 1] = current[2]
    #full matrix O(n^2) iteration
    for iter in range(n):
        marked, weight_map = [0] * n, [float("inf")] * n
        weight_map[iter] = 0
        current_vertex_weight = float("inf")
        current_vertex = None
        for _ in range(n):
            current_vertex, current_vertex_weight = None, float("inf")
        #find min_weight vertex
            for i in range(n):
                if not marked[i] and weight_map[i] < current_vertex_weight:
                        current_vertex, current_vertex_weight  = i, weight_map[i]
            if current_vertex_weight == float("inf"): break
            for i in range(n):
                weight_map[i] = min(weight_map[i], weight_map[current_vertex] + matrix[current_vertex][i])
            marked[current_vertex] = 1
        matrix[iter] = weight_map
    for row in matrix:
        print(' '.join([str(elem) for elem in row]), file=file_output)
    file_output.close()

thread = threading.Thread(target=main)
thread.start()