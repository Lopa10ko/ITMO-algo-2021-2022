from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(3 * 67108864)

def main(): #Levenstein readaction diff
    first, second = input().strip(), input().strip()
    matrix = [["" for _ in range(len(second))] for i in range(len(first))]
    for i in range(len(first)):
        for j in range(len(second)):
            if first[i] == second[j]:
                matrix[i][j] = first[i] if i == 0 or j == 0 else matrix[i-1][j-1] + first[i]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], key=len)
    print(matrix[-1][-1] if matrix[-1][-1] != "" else '\n')
thread = threading.Thread(target=main)
thread.start()