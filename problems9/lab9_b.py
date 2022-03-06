from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(2 * 67108864)
 
def main():
    file_input, file_output = open('cycle.in', 'r'), open('cycle.out','w')
    #dfs for each vertex in V
    #if we can reach grey(1) vertex, cycle exists
    cycle = []
    def dfs(index):
        nonlocal cycle
        contig_lst[index][0] = 1
        cycle.append(index + 1)
        #avoid current_vertex flush
        nonlocal current_vertex
        for i in range(1, len(contig_lst[index])):
            if contig_lst[contig_lst[index][i]][0] == 0:
                if dfs(contig_lst[index][i]): return True
            elif contig_lst[contig_lst[index][i]][0] == 1:
                current_vertex = contig_lst[index][i] + 1
                return True
        cycle = cycle[:-1]
        contig_lst[index][0] = 2

    n, m = map(int, file_input.readline().split())
    contig_lst = [[0] for _ in range(n)]
    flag = 0
    current_vertex = 0
    #contigious vertexes list creation i: [color, *[ends_values]]
    for _ in range(m):
        current = list(map(int, file_input.readline().split()))
        contig_lst[current[0] - 1].append(current[1] - 1)
    for index in range(len(contig_lst)):
        # print(*contig_lst)
        if contig_lst[index][0] == 0:
            if dfs(index):
                print('YES', file=file_output)
                print(*[cycle[i] for i in range(cycle.index(current_vertex), len(cycle))], file=file_output)
                flag = 1
                break
    if not flag: 
        print('NO', file=file_output)
    file_output.close()

thread = threading.Thread(target=main)
thread.start()