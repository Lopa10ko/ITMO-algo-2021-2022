from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(2 * 67108864)
 
def main():
    file_input, file_output = open('bipartite.in', 'r'), open('bipartite.out','w')
    #dfs for each vertex in V
    #if we can reach grey(1) vertex, cycle exists
    def dfs(index, color):
        contig_lst[index][0] = color
        for i in range(1, len(contig_lst[index])):
            if contig_lst[contig_lst[index][i]][0] is None:
                if dfs(contig_lst[index][i], not color): return True
            elif contig_lst[contig_lst[index][i]][0] == color:
                print('NO', file=file_output)
                return True

    n, m = map(int, file_input.readline().split())
    contig_lst = [[None] for _ in range(n)]
    flag = 0
    #contigious vertexes list creation i: [color, *[ends_values]]
    for _ in range(m):
        current = list(map(int, file_input.readline().split()))
        contig_lst[current[0] - 1].append(current[1] - 1)
        contig_lst[current[1] - 1].append(current[0] - 1)
    for index in range(len(contig_lst)):
        if contig_lst[index][0] is None and dfs(index, 1):
            flag = 1
            break
    if not flag: 
        print('YES', file=file_output)
    file_output.close()

thread = threading.Thread(target=main)
thread.start()