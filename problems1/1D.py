file_input = open('sortland.in', 'r')
file_output = open('sortland.out', 'w')

n = int(file_input.readline())
arr = list(map(float, file_input.readline().split()))
unsorted_arr = arr.copy()
for i in range(1, n):
    tmp = arr[i]
    j = i - 1
    while j >= 0 and arr[j] >= tmp:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = tmp
    
print(unsorted_arr.index(arr[0]) + 1,
      unsorted_arr.index(arr[n // 2]) + 1,
      unsorted_arr.index(arr[-1]) + 1, file=file_output)

file_output.close()
