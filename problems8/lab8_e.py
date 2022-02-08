from sys import setrecursionlimit
import threading
import queue
setrecursionlimit(10 ** 9)
threading.stack_size(67108864)

def main():
    file_input, file_output = open('pathbge1.in', 'r'), open('pathbge1.out','w')
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
    graph = {}
    #contigious vortexes list creation in dict
    for _ in range(m):
        current = list(map(int, file_input.readline().split()))
        if graph.get(current[0] - 1) is not None and current[1] - 1 not in graph.get(current[0] - 1):
            graph.update({current[0] - 1 : graph.get(current[0] - 1) + [current[1] - 1]})
        elif graph.get(current[0] - 1) is None:
            graph.update({current[0] - 1 : [current[1] - 1]})
        if graph.get(current[1] - 1) is not None and current[0] - 1 not in graph.get(current[1] - 1):
            graph.update({current[1] - 1 : graph.get(current[1] - 1) + [current[0] - 1]})
        elif graph.get(current[1] - 1) is None:
            graph.update({current[1] - 1 : [current[0] - 1]})
    # print(graph)
    print(*bfs(graph, 0, n), file=file_output)
    file_output.close()

thread = threading.Thread(target=main)
thread.start()