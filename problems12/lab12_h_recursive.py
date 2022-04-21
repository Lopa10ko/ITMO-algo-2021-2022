from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(3 * 67108864)

def main(): #time O(n^2)
    def get_pali(left, right):
        nonlocal matrix
        if matrix[left][right] == -1:
            if seq[left] == seq[right]:
                matrix[left][right] = get_pali(left + 1, right) + get_pali(left, right - 1) + 1
            else:
                matrix[left][right] = get_pali(left + 1, right) + get_pali(left, right - 1) - get_pali(left + 1, right - 1)
        return matrix[left][right] % 10 ** 9
    n = int(input())
    seq = [int(i) for i in input().split()]
    # seq = ''.join([str(elem) for elem in list(map(int, input().split()))])
    #number of palindromic subseq
    matrix = [[1 if i == j else 0 if j < i else -1 for j in range(n)] for i in range(n)]
    print(get_pali(0, n - 1) % 10 ** 9)
thread = threading.Thread(target=main)
thread.start()