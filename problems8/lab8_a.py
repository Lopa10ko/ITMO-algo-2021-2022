from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(67108864)

def main():
    file_input, file_output = open('input.txt', 'r'), open('output.txt','w')

    n, m = map(int, file_input.readline().split())
    vortex = [list(map(int, file_input.readline().split())) for _ in range(m)]
    matrix = [[1 if [layer, length] in vortex else 0 for length in range(1, n + 1)] for layer in range(1, n + 1)]
    print(*[' '.join(map(str, elem)) for elem in matrix], sep='\n', file=file_output)
    file_output.close()

thread = threading.Thread(target=main)
thread.start()