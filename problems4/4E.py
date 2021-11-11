file_input = open('binsearch.in', 'r')
file_output = open('binsearch.out', 'w')
 
#binary left search for sorted data
def get_first(arr, key):
    left, right = -1, len(arr)
    while right > left + 1:
        mid = (left + right) // 2
        if arr[mid] < key:
            left = mid
        else:
            right = mid
    if right == len(arr):
        return -1
    if arr[right] == key:
        return right + 1
    return -1
  
#binary right search for sorted data
def get_last(arr, key):
    left, right = -1, len(arr)
    while right > left + 1:
        mid = (left + right) // 2
        if arr[mid] <= key:
            left = mid
        else:
            right = mid
    if left == -1:
        return -1
    if arr[left] == key:
        return left + 1
    return -1
  
n = int(file_input.readline())
data = [int(x) for x in file_input.readline().split()]
m = int(file_input.readline())
request = [int(x) for x in file_input.readline().split()]
for i in range(m):
    print(get_first(data, request[i]), get_last(data, request[i]), file=file_output)
  
file_output.close()
