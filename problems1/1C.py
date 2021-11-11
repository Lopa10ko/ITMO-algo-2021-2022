file_input = open('smallsort.in', 'r')
file_output = open('smallsort.out', 'w')

n = int(file_input.readline())
arr = list(map(int, file_input.readline().split()))
for i in range(1, n):
    tmp = arr[i]
    j = i - 1
    while j >= 0 and arr[j] >= tmp:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = tmp

print(*arr, file=file_output)
file_output.close()
