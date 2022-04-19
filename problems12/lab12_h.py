from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(3 * 67108864)

def main(): #time O(n^2)
    n = int(input())
    seq = ''.join([str(elem) for elem in list(map(int, input().split()))])
    #number of palindromic subseq
    matrix = [[0 for _ in range(n + 2)] for i in range(n + 2)]
    for i in range(n): matrix[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n):
            temp_len = length + i - 1
            if (temp_len < n):
                #seq[...] == seq[...]: [s] = [.s] + [s.] + 1
                #else                  [s] = [.s] + [s.] - [.s.]
                matrix[i][temp_len] = matrix[i][temp_len - 1] + matrix[i + 1][temp_len] + 1 if seq[i] == seq[temp_len] else matrix[i][temp_len - 1] + matrix[i + 1][temp_len] - matrix[i + 1][temp_len - 1]
    print(matrix[0][n - 1] % 10 ** 9)
thread = threading.Thread(target=main)
thread.start()