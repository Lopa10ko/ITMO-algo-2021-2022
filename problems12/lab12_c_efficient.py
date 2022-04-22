from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(3 * 67108864)

def main(): #Hunt–Szymanski
    # first, second = input().strip(), input().strip()
    first, second = "abacabadabacaba", "dbdccdbd"
    def lcs(B, A):
        m, n = len(A) , len(B)
        T = [[0 for _ in range(n + 1)] for _ in range(2)]
        for i in range(m - 1, -1, -1):
            ndx = i & 1
            for j in range(n - 1, -1, -1):
                if A[i] == B[j]: T[ndx][j] = T[1 - ndx][j + 1] + 1
                else: T[ndx][j] = max(T[1 - ndx][j], T[ndx][j + 1])
        seq_len = T[0][0]
        print(T[0][0])
        print(T)
        # i, j = m, n
        # ans = '' * seq_len
        # while i > 0 and j > 0:
        #     ndx = i & 1
        #     if A[i - 1] == B[j - 1]:
        #         ans[seq_len - 1] = A[i - 1]
        #         i -= 1
        #         j -= 1
        #         seq_len -= 1
        #     elif T[1 - ndx][j] > T[ndx][j + 1]: i-= 1
        #     else: j-=1

    print(lcs(first, second) if len(first) > len(second) else lcs(second, first))
thread = threading.Thread(target=main)
thread.start()