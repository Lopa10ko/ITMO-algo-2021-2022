from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(67108864)

def main():
    file_input, file_output = open('input.txt', 'r'), open('output.txt','w')

    n, flag = int(file_input.readline()), 1
    matrix = [list(map(int, file_input.readline().split())) for _ in range(n)]
    for index in range(n):
        if matrix[index][index] == 1:
            flag = 0
            break
        for layer in range(index):
            if matrix[index][layer] != matrix[layer][index]:
                flag = 0 
                break
    print("YES" if flag == 1 else "NO", file=file_output)
    file_output.close()

thread = threading.Thread(target=main)
thread.start()