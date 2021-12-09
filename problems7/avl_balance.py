from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(67108864)

def main():
    file_input=open('balance.in', 'r')
    file_output=open('balance.out','w')

    n = int(file_input.readline())
    avl_array, heights = [], [0] * n

    def get_height(avl_ptr):
        #global heights
        left, right = avl_array[avl_ptr][1], avl_array[avl_ptr][2]
        if heights[avl_ptr]:
            return heights[avl_ptr]
        if left == -1 and right == -1:
            heights[avl_ptr] = 1
            return 1
        elif left == -1:
            heights[avl_ptr] = get_height(right) + 1
            return heights[avl_ptr]
        elif right == -1:
            heights[avl_ptr] = get_height(left) + 1
            return heights[avl_ptr]
        heights[avl_ptr] = max(get_height(left), get_height(right)) + 1
        return heights[avl_ptr]

    for i in range(n):
        avl_array.append([elem - 1 for elem in list(map(int, file_input.readline().split()))])
    balance=[]
    for i in range(n - 1, -1, -1):
        li, ri, left_height, right_height = avl_array[i][1], avl_array[i][2], 0, 0
        if li != -1:
            left_height = get_height(li)
        if ri != -1:
            right_height = get_height(ri)
        balance.append(right_height - left_height)
    print(*reversed(balance), sep = '\n', file=file_output)
        # for i in range(n-1,-1,-1):
        #     print(answer[i], file=file_output)
    file_output.close()

thread = threading.Thread(target=main)
thread.start()