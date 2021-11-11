file_input = open('sort.in', 'r')
file_output = open('sort.out', 'w')

def merge(arr):
    if len(arr) in [0,1]: return arr
    left_arr, right_arr = arr[:len(arr) // 2], arr[len(arr) // 2:]
    merge(left_arr)
    merge(right_arr) 
    left_cnt, right_cnt, cnt = 0, 0, 0
    merge_arr = [0] * (len(left_arr) + len(right_arr))
    while left_cnt < len(left_arr) and right_cnt < len(right_arr):
        if left_arr[left_cnt] <= right_arr[right_cnt]:
            merge_arr[cnt] = left_arr[left_cnt]
            left_cnt += 1
        else:
            merge_arr[cnt] = right_arr[right_cnt]
            right_cnt += 1
        cnt += 1
    while right_cnt < len(right_arr):
        merge_arr[cnt] = right_arr[right_cnt]
        right_cnt += 1
        cnt += 1
    while left_cnt < len(left_arr):
        merge_arr[cnt] = left_arr[left_cnt]
        left_cnt += 1
        cnt += 1
    for i in range(len(arr)):
        arr[i] = merge_arr[i]
    return arr

n = int(file_input.readline())
arr = list(map(int, file_input.readline().split()))

print(*merge(arr), file = file_output)
file_output.close()
