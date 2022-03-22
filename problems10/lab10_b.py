from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(67108864)
 
def main():
    file_input, file_output = open('topsort.in', 'r'), open('topsort.out','w')
    #dfs for each vertex in V; vertex_f --> time
    #for each all-done vertex push to linked_lst
    def dfs(index):
        contig_lst[index][0] = 1
        for i in range(1, len(contig_lst[index])):
            if contig_lst[contig_lst[index][i]][0] == 0:
                if dfs(contig_lst[index][i]): return True
            elif contig_lst[contig_lst[index][i]][0] == 1: return True
        contig_lst[index][0] = 2
        linked_lst.append(index + 1)

    n, m= map(int, file_input.readline().split())
    contig_lst, linked_lst= [[0] for _ in range(n)], []
    flag = 0
    #contigious vertexes list creation i: [color, *[ends_values]]
    for _ in range(m):
        current = list(map(int, file_input.readline().split()))
        contig_lst[current[0] - 1].append(current[1] - 1)
    for index in range(len(contig_lst)):
        # print(*contig_lst)
        if contig_lst[index][0] == 0:
            if dfs(index):
                print(-1, file=file_output)
                flag = 1
                break
    if not flag: 
        print(*linked_lst[::-1], sep=' ', file=file_output)
    file_output.close()

thread = threading.Thread(target=main)
thread.start()