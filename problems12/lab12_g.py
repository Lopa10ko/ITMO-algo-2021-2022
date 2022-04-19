from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(3 * 67108864)

def main(): #O(sn)
    file_input, file_output = open("knapsack.in", 'r'), open("knapsack.out", 'w')
    s, n = map(int, file_input.readline().split())
    #d[i][j]: elems numeration - weights (bool)
    weights = list(map(int, file_input.readline().split()))
    dp = [[0 for _ in range(s + 1)] for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(0, s + 1):
            if dp[i - 1][j]:
                dp[i][j] = 1
                if j + weights[i - 1] <= s:
                    dp[i][j + weights[i - 1]] = 1
    for i in range(s, -1, -1):
        if dp[n][i]:
            print(i, file=file_output)
            break
    file_output.close()

thread = threading.Thread(target=main)
thread.start()
