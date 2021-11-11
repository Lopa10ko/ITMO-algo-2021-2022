file_input = open('isheap.in', 'r')
file_output = open('isheap.out', 'w')
flag = "YES"
n = int(file_input.readline())
arr = list(map(int, file_input.readline().split()))
for i in range(1, n):
    if 2*i <= n:
        if arr[i - 1] > arr[2*i - 1]:
            flag = "NO"
            break
    if 2*i + 1 <= n:
        if arr[i - 1] > arr[2*i]:
            flag = "NO"
            break
print(flag, file=file_output)
file_output.close()
