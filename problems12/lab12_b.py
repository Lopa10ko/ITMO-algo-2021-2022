from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(3 * 67108864)

def main(): #Knuth LIS-binsearch algo O(nlogn)
    def binsearch():
        left, right = 1, largest + 1
        while right - left > 1:
            mid = (left + right) // 2
            if data[sub[mid]] < data[i]: left = mid
            else: right = mid
        return left
    n = int(input())
    data = [None] + list(map(int, input().split()))
    # [list] sub[i]: index(min last element) in sequence of len == i
    # [list] parent[k]: index of predecessor of sub[k] in LIS ending at sub[k]
    sub, parent = [None] * (n + 1), [None] * (n + 1)
    largest = 0
    for i in range(1, n + 1):
        aim = 0 if (largest == 0 or data[sub[1]] >= data[i]) else binsearch()
        parent[i] = sub[aim]
        if aim == largest or data[sub[aim + 1]] > data[i]:
            sub[aim + 1] = i
            largest = max(largest, aim + 1)
    ans, index = [], sub[largest]
    while largest > 0:
        ans.append(data[index])
        index = parent[index]
        largest -= 1
    print(len(ans))
    print(*ans[::-1])

thread = threading.Thread(target=main)
thread.start()