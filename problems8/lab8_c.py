from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(67108864)
 
def main():
    file_input, file_output = open('input.txt', 'r'), open('output.txt','w')
    def rescale(lst):
        return [lst[1], lst[0]] if lst[1] < lst[0] else lst
    n, m = map(int, file_input.readline().split())
    flag = 0
    vortex = [tuple(rescale(list(map(int, file_input.readline().split())))) for _ in range(m)]
    print("YES" if len(set(vortex)) != len(vortex) and n != 0 else "NO", file=file_output)
    file_output.close()
 
thread = threading.Thread(target=main)
thread.start()