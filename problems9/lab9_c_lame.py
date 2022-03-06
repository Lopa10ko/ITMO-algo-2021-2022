from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(2 * 67108864)
 
def main():
    file_input, file_output = open('bipartite.in', 'r'), open('bipartite.out','w')
    #dfs on set to find all cycles
    def dfs(contig_lst, first, last):
        condition = [(first, [])]
        while condition:
            position, cycle = condition.pop()
            if position == last and cycle:
                yield cycle
                continue
            for current_pos in contig_lst[position]:
                if current_pos in cycle: continue
                condition.append((current_pos, cycle + [current_pos]))

    n, m = map(int, file_input.readline().split())
    contig_lst = {}
    flag = 0
    #contigious vertexes list creation i: [color, *[ends_values]]
    for _ in range(m):
        current = list(map(int, file_input.readline().split()))
        if contig_lst.get(current[0] - 1) is not None and current[1] - 1 not in contig_lst.get(current[0] - 1):
            contig_lst.update({current[0] - 1 : contig_lst.get(current[0] - 1) + [current[1] - 1]})
        elif contig_lst.get(current[0] - 1) is None:
            contig_lst.update({current[0] - 1 : [current[1] - 1]})
        if contig_lst.get(current[1] - 1) is not None and current[0] - 1 not in contig_lst.get(current[1] - 1):
            contig_lst.update({current[1] - 1 : contig_lst.get(current[1] - 1) + [current[0] - 1]})
        elif contig_lst.get(current[1] - 1) is None:
            contig_lst.update({current[1] - 1 : [current[0] - 1]})
    #if v1-...-v1 cycle's len is even, then "NO"
    for vertex in contig_lst:
        for cycle in dfs(contig_lst, vertex, vertex):
            if len([vertex] + cycle) % 2 == 0:
                print('NO', file=file_output)
                flag = 1
                break
        if flag: break
    if not flag: print('YES', file=file_output)
    file_output.close()

thread = threading.Thread(target=main)
thread.start()