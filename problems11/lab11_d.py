from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(3 * 67108864)

def main():
    inf = 10 ** 15 + 1
    #Ford-Bellman algo
    def get_marked(vertex):
        marked[vertex] = 1
        for current_vertex in matrix[vertex]:
            if not marked[current_vertex]: get_marked(current_vertex)
    
    file_input, file_output = open('path.in', 'r'), open('path.out','w')
    n, m, s = map(int, file_input.readline().split())
    weight_map, bad_weights, matrix, marked = [inf] * n, [], [[] for _ in range(n)], [0] * n
    weight_map[s - 1] = 0
    all_data = []
    for _ in range(m):
        current = list(map(int, file_input.readline().split()))
        matrix[current[0] - 1].append(current[1] - 1)
        all_data.append([current[0] - 1, current[1] - 1, current[2]])
    for _ in range(n + 1):
        bad_weights = []
        flag = None
        for i in range(m):
            current = all_data[i]
            if weight_map[current[0]] != inf:
                if weight_map[current[1]] > weight_map[current[0]] + current[2]:
                    weight_map[current[1]] = weight_map[current[0]] + current[2]
                    flag = current[1]
                    bad_weights.append(current[1])
        if flag is None: break
    if flag:
        for vertex1 in bad_weights:
            if not marked[vertex1]: get_marked(vertex1)
    for j in range(n):
        if marked[j]: weight_map[j] = '-'
    for weight in weight_map:
        if weight != inf: print(weight, file=file_output)
        else: print('*', file=file_output)
    file_output.close()

thread = threading.Thread(target=main)
thread.start()