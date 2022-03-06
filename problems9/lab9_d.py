from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(2 * 67108864)
 
def main():
    file_input, file_output = open('cond.in', 'r'), open('cond.out','w')
    #std Kosaraju's condensation algo
    #dfs1 forms a sequence tout by the exit-times of dfs algo -- topsort
    tout, component = [], []
    def dfs_ordering(vertex):
        colored[vertex] = [True]
        for i in range(len(contig_lst[vertex])):
            if not colored[contig_lst[vertex][i]]:
                dfs_ordering(contig_lst[vertex][i])
        tout.append(vertex)
    #dfs in transposed contig_lst
    #dfs2 walks on iverted graph from tout[0]
    def dfs_backshift(vertex):
        colored[vertex] = [True]
        component.append(vertex)
        for i in range(len(reversed_lst[vertex])):
            if not colored[reversed_lst[vertex][i]][0]: dfs_backshift(reversed_lst[vertex][i])

    n, m = map(int, file_input.readline().split())
    contig_lst, reversed_lst = [[] for _ in range(n)], [[] for _ in range(n)]
    colored = [False for _ in range(n)]
    component_number = 1
    answer = [0 for _ in range(n)]
    #contigious vertexes list and transposed list creation
    for _ in range(m):
        current = list(map(int, file_input.readline().split()))
        contig_lst[current[0] - 1].append(current[1] - 1)
        reversed_lst[current[1] - 1].append(current[0] - 1)
    for index in range(len(contig_lst)):
        if not colored[index]: dfs_ordering(index)
    colored = [[False] for _ in range(n)]
    for index in range(len(reversed_lst)):
        if not colored[tout[n - index - 1]][0]:
            dfs_backshift(tout[n - index - 1])
            for i in component:
                answer[i] = component_number
            component_number += 1
            component.clear()
    print(component_number - 1, file=file_output)
    print(*answer, file=file_output)
    file_output.close()

thread = threading.Thread(target=main)
thread.start()