from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(67108864)
 
def main():
    file_input, file_output = open('game.in', 'r'), open('game.out','w')
    n, m, s = map(int, file_input.readline().split())
    contig_lst, reversed_lst = [[] for _ in range(n)], [[] for _ in range(n)]
    strategy_lst = [0] * n
    #transposed and normal contigious vertexes lists
    for _ in range(m):
        current = list(map(int, file_input.readline().split()))
        contig_lst[current[0] - 1].append(current[1] - 1)
        reversed_lst[current[1] - 1].append(current[0] - 1)
    #isolated vertexes - our goal (code +- to indicate winnable vertexes)
    to_visit, temp_pool = [], []
    for index in range(n):
        if not len(contig_lst[index]):
            to_visit.append(index)
            strategy_lst[index] = -1
    while to_visit:
        current_vertex = to_visit.pop()
        for vertex in reversed_lst[current_vertex]:
            if not strategy_lst[vertex]:
                strategy_lst[vertex] = -strategy_lst[current_vertex]
                temp_pool.append(vertex)
            elif strategy_lst[vertex] == -1 and strategy_lst[current_vertex] == -1:
                strategy_lst[vertex] == 1
                temp_pool.append(vertex)
        if not len(to_visit):
            to_visit, temp_pool = temp_pool[:], []
    print('First player wins' if strategy_lst[s - 1] == 1 else 'Second player wins', file=file_output)
    file_output.close()

thread = threading.Thread(target=main)
thread.start()