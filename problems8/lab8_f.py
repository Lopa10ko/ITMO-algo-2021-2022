from platform import mac_ver
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
    start, finish = [], []
    mapping = []
    prepath, distance = [[0] * m] * n, [[None] * m] * n
    for i in range(n):        
        current = file_input.readline()[: m]
        current = current.replace('.', '1').replace('#', '0')
        if 'S' in current:
            start = [i, current.find('S')]
            current = current.replace('S', '1', 1)
        if 'T' in current:
            finish = [i, current.find('T')]
            current = current.replace('T', '1', 1)
        mapping.append(list(current))
    

    

        
    # print(graph)
    # print(*bfs(graph, 0, n), file=file_output)
    file_output.close()

thread = threading.Thread(target=main)
thread.start()