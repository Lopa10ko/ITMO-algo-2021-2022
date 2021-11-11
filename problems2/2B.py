file_input = open('race.in', 'r')
file_output = open('race.out', 'w')

n = int(file_input.readline())
protocol = [list(map(str, file_input.readline().split())) for i in range(n)]


def sort_by_letters(arr):
    if len(arr) in [0, 1]: return arr
    left_arr, right_arr = arr[:len(arr) // 2], arr[len(arr) // 2:]
    sort_by_letters(left_arr)
    sort_by_letters(right_arr)
    left_cnt, right_cnt, cnt = 0, 0, 0
    merge_arr = [0] * (len(left_arr) + len(right_arr))
    while left_cnt < len(left_arr) and right_cnt < len(right_arr):
        if left_arr[left_cnt][0] <= right_arr[right_cnt][0]:
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


protocol = sort_by_letters(protocol)
print('=== ' + protocol[0][0] + ' ===', file=file_output)
print(protocol[0][1], file=file_output)
for i in range(1, len(protocol)):
    if protocol[i][0] != protocol[i - 1][0]:
        print('=== ' + protocol[i][0] + ' ===', file=file_output)
        print(protocol[i][1], file=file_output)
    else:
        print(protocol[i][1], file=file_output)

file_input.close()
file_output.close()
