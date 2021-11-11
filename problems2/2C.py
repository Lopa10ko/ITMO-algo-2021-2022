import copy
file_input = open('inversions.in', 'r')
file_output = open('inversions.out', 'w')
#merge in other realization

def merge_inversions(arr, sequence, begin_index, left_chunk, end_index):
    left_cnt, right_cnt, local_cnt, cnt = begin_index, left_chunk + 1, 0, begin_index
    while left_cnt <= left_chunk and right_cnt <= end_index:
        if arr[left_cnt] <= arr[right_cnt]:
            sequence[cnt] = arr[left_cnt]
            left_cnt += 1
            cnt += 1
        else:
            sequence[cnt] = arr[right_cnt]
            local_cnt += left_chunk - left_cnt + 1
            right_cnt += 1
            cnt += 1
    while left_cnt <= left_chunk:
        sequence[cnt] = arr[left_cnt]
        left_cnt += 1
        cnt += 1
    while right_cnt <= end_index:
        sequence[cnt] = arr[right_cnt]
        right_cnt += 1
        cnt += 1
    for i in range(begin_index, end_index+1): arr[i] = sequence[i]
    return local_cnt
    
def get_inversions(arr, sequence, begin_index, end_index):
    local_cnt = 0
    if end_index - begin_index > 0: 
        local_cnt += get_inversions(arr, sequence, begin_index, (begin_index + end_index) // 2) + get_inversions(arr, sequence, (begin_index + end_index) // 2 + 1, end_index)
        local_cnt += merge_inversions(arr, sequence, begin_index, (begin_index + end_index) // 2, end_index)
    return local_cnt

    
n = int(file_input.readline())
arr = list(map(int, file_input.readline().split()))
sequence = [''] * n
print(get_inversions(arr, sequence, 0, n - 1), file = file_output)
file_output.close()
