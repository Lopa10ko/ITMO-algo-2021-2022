from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(67108864)
 
def main():
    file_input, file_output = open('components.in', 'r'), open('components.out','w')
    #recursive depth-first-search
    def dfs(index, cnt):
        components[index][0], components[index][1] = 1, cnt
        for i in range(len(contig_lst[index])):
            if not components[contig_lst[index][i]][0]:
                dfs(contig_lst[index][i], cnt)
 
    n, m = map(int, file_input.readline().split())
    cnt = 1
    contig_lst, components = [[] for _ in range(n)], [[0, -1] for _ in range(n)]
    #contigious vortexes list creation
    for _ in range(m):
        current = list(map(int, file_input.readline().split()))
        if current[0] - 1 not in contig_lst[current[1] - 1]:
            contig_lst[current[1] - 1].append(current[0] - 1)
        if current[1] - 1 not in contig_lst[current[0] - 1]:
            contig_lst[current[0] - 1].append(current[1] - 1)
    for index in range(n):
        if not components[index][0]:
            dfs(index, cnt)
            cnt += 1
    print(cnt - 1, file=file_output)
    print(*[components[index][1] for index in range(n)], end=' ', file=file_output)
    file_output.close()
 
thread = threading.Thread(target=main)
thread.start()