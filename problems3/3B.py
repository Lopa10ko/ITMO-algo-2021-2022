file_input = open('sort.in', 'r')
file_output = open('sort.out', 'w')
 
def get_heap(arr, length, index):
    left = 2 * index + 1
    right, max_index = left + 1, index
    if left < length:
        if arr[max_index] < arr[left]: max_index = left
    if right < length:
        if arr[max_index] < arr[right]: max_index = right
    if max_index != index:
        arr[max_index], arr[index] = arr[index], arr[max_index]
        get_heap(arr, length, max_index)
 
def heap_sort(arr, length):
    for i in range(length // 2 - 1, -1, -1):
        get_heap(arr, length, i)
    for i in range(length - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        get_heap(arr, i, 0)
 
 
n = int(file_input.readline())
arr = list(map(int, file_input.readline().split()))
heap_sort(arr, n)
print(*arr, file=file_output)
file_output.close()
