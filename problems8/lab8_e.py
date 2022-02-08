from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(67108864)

def main():
    file_input, file_output = open('pathbge1.in', 'r'), open('pathbge1.out','w')
    #recursive depth-first-searchw with dist minimization
    def dfs(index, dist):
        components[index][0] = 1 #colored grey
        if components[index][1] is None or components[index][1] > dist:
            components[index][1] = dist
        for i in range(len(contig_lst[index])):
            if contig_lst[index][i] and not components[contig_lst[index][i]][0]:
                dfs(contig_lst[index][i], dist +1)

    n, m = map(int, file_input.readline().split())
    contig_lst, components = [[] for _ in range(n)], [[0, None] for _ in range(n)]
    #contigious vortexes list creation
    for _ in range(m):
        current = list(map(int, file_input.readline().split()))
        if current[0] - 1 not in contig_lst[current[1] - 1]:
            contig_lst[current[1] - 1].append(current[0] - 1)
        if current[1] - 1 not in contig_lst[current[0] - 1]:
            contig_lst[current[0] - 1].append(current[1] - 1)
    dfs(0, 0)
    print(*[components[index][1] for index in range(n)], end=' ', file=file_output)
    file_output.close()

thread = threading.Thread(target=main)
thread.start()