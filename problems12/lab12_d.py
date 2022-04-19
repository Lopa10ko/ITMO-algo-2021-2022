from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(3 * 67108864)

def main():
    def cover():
        nonlocal i, j
        while i >= 0 and j >= 0 and j < m:
            moves = 0
            for step in [[1, -2], [-2, 1], [-1, -2], [-2, -1]]:
                di, dj = step[0] + i, step[1] + j
                if di in range(n) and dj in range(m) and matrix[di][dj] > 0:
                    moves += matrix[di][dj]
            matrix[i][j] += moves
            i -= 1
            j += 1
    file_input, file_output = open('knight2.in', 'r'), open('knight2.out','w')
    n, m = map(int, file_input.readline().split())
    matrix = [[0] * m for _ in range(n)]
    matrix[0][0] = 1
    for diff in range(n):
        i, j = diff, 0
        cover()
    for diff in range(1, m):
        i, j = n - 1, diff
        cover()
    print(matrix[-1][-1], file=file_output)
    file_output.close()

thread = threading.Thread(target=main)
thread.start()