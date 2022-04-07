from asyncio.windows_events import NULL
from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(3 * 67108864)

def main():
    inf = 10 ** 9
    #Ford-Bellman algo https://e-maxx.ru/algo/negative_cycle
    file_input, file_output = open('negcycle.in', 'r'), open('negcycle.out','w')
    n = int(file_input.readline())
    weight_map, matrix, negcycle = [0] * n, [], [None] * n
    for i in range(n):
        current = list(map(int, file_input.readline().split()))
        # concurrent = []
        for j in range(n):
            if current[j] != inf: matrix.append([i, j, current[j]])
        # matrix[i] = concurrent
        # del concurrent
    flag = None
    for i in range(n):
        for j in range(len(matrix)):
            if weight_map[matrix[j][1]] > matrix[j][2] + weight_map[matrix[j][0]]:
                negcycle[matrix[j][1]], flag = matrix[j][:2]
                weight_map[matrix[j][1]] = matrix[j][2] + weight_map[matrix[j][0]]
        if flag is None: break
    if flag is not None:
        all_flag = flag
        for _ in range(n): all_flag = negcycle[all_flag]
        all_negcycle = []
        iter = all_flag
        while 1:
            all_negcycle.append(iter)
            iter = negcycle[iter]
            if all_flag == iter: break
        all_negcycle.append(all_flag)
        all_negcycle = all_negcycle[::-1]
        print('YES', len(all_negcycle), sep = '\n', file=file_output)
        print(*[vertex + 1 for vertex in all_negcycle], file=file_output)
    else: print('NO', file=file_output)
    file_output.close()

thread = threading.Thread(target=main)
thread.start()