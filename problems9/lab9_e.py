from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(3 * 67108864)
  
def main():
    file_input, file_output = open('hamiltonian.in', 'r'), open('hamiltonian.out','w')
    #dfs for each vertex in V; vertex_f --> time
    #if you can walk by vertexes in topsorted linked_lst, then graph is hamiltonian
    def dfs(index):
        contig_lst[index][0] = 'g'
        for i in range(1, len(contig_lst[index])):
            if contig_lst[contig_lst[index][i]][0] == 'w':
                if dfs(contig_lst[index][i]): return True
            elif contig_lst[contig_lst[index][i]][0] == 'g': return True
        contig_lst[index][0] = 'b'
        linked_lst.append(index)
 
    n, m= map(int, file_input.readline().split())
    contig_lst, linked_lst= [['w'] for _ in range(n)], []
    flag = 0
    # all_values = []
    #contigious vertexes list creation i: [color, *[ends_values]]
    for _ in range(m):
        current = list(map(int, file_input.readline().split()))
        contig_lst[current[0] - 1].append(current[1] - 1)
        # all_values.append(current)
    for index in range(len(contig_lst)):
        if contig_lst[index][0] == 'w':
            if dfs(index):
                print('NO', file=file_output)
                flag = 1
                break
    #check for (vi,vj) from linked_lst
    if not flag:
        reversed_linked = linked_lst[::-1]
        for i in range(len(linked_lst) - 1):
            if reversed_linked[i + 1] not in contig_lst[reversed_linked[i]] or len(linked_lst) != n:
                flag = 1
                break
        if not flag:
            print('YES', file=file_output)
        else:
            print('NO', file=file_output)
    file_output.close()
 
thread = threading.Thread(target=main)
thread.start()