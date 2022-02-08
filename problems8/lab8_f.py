from sys import setrecursionlimit
import threading
import queue
setrecursionlimit(10 ** 9)
threading.stack_size(67108864)

def main():
    file_input, file_output = open('input.txt', 'r'), open('output.txt','w')
    #non-recursive depth-first-searchw with dist minimization
    def bfs(graph, source, n):
        visited, distances, que  = [], [0] * n, queue.Queue()
        que.put(source)
        while not que.empty(): 
            temp = que.get()
            visited.append(temp)
            for index in graph.get(temp):
                if distances[index] == 0:
                    distances[index] = distances[temp] + 1
                    que.put(index)
        distances[0] = 0
        return distances

    n, m = map(int, file_input.readline().split())
    # graph = {(elem, j) : [] for j in range(m) for elem in file_input.readline() if elem != "#"}
    start, finish, mapping, answer = [], [], [], []
    prepath, value = [[0 for i in range(m)] for _ in range(n)], [[None for i in range(m)] for _ in range(n)]
    for i in range(n):        
        current = file_input.readline()[: m]
        current = current.replace('.', '1').replace('#', '0')
        if 'S' in current:
            start = [i, current.find('S')]
            current = current.replace('S', '1', 1)
        if 'T' in current:
            finish = [i, current.find('T')]
            current = current.replace('T', '1', 1)
        mapping.append(list(map(int, current)))
    # print(mapping)
    que = queue.Queue()
    que.put(start)
    value[start[0]][start[1]] = 0
    while not que.empty():
        # print(finish)
        i, j = que.get()
        if i - 1 > -1:
            if mapping[i - 1][j] and not value[i - 1][j]: 
                value[i - 1][j] = value[i][j] + 1
                prepath[i - 1][j] = 'U'
                que.put([i - 1, j])
        if j - 1 > -1:
            if mapping[i][j - 1] and not value[i][j - 1]: 
                value[i][j - 1] = value[i][j] + 1
                prepath[i][j - 1] = 'L'
                que.put([i, j - 1])
        if i + 1 < n:
            if mapping[i + 1][j] and not value[i + 1][j]: 
                value[i + 1][j] = value[i][j] + 1
                prepath[i + 1][j] = 'D'
                que.put([i + 1, j])
        if j + 1 < m:
            if mapping[i][j + 1] and not value[i][j + 1]: 
                value[i][j + 1] = value[i][j] + 1
                prepath[i][j + 1] = 'R'
                que.put([i, j + 1])
        if value[finish[0]][finish[1]] is not None: break
    i, j = finish
    # print(prepath)
    if not value[finish[0]][finish[1]]: print(-1, file=file_output)
    else:
        print(value[i][j], file=file_output)
    # print(graph)
    # print(*bfs(graph, 0, n), file=file_output)
        for _ in range(value[i][j]):
            if prepath[i][j] == 'U':
                answer.append('U')
                i += 1
            elif prepath[i][j] == 'L':
                answer.append('L')
                j += 1
            elif prepath[i][j] == 'D':
                answer.append('D')
                i -= 1
            elif prepath[i][j] == 'R':
                answer.append('R')
                j -= 1
        print(*answer[::-1], sep='', file=file_output)
    file_output.close()

thread = threading.Thread(target=main)
thread.start()