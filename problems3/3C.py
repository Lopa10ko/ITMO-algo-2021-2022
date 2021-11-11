file_input = open('radixsort.in', 'r')
file_output = open('radixsort.out', 'w')
#LSD
def get_radix_kth(arr, m, k):
    buffer_arr, buffer_elements = [0] * m, ['q'] * len(arr)
    for i in range(len(arr)):
        buffer_arr[ord(arr[i][k]) - ord('a')] += 1
    for i in range(1, m):
        buffer_arr[i] += buffer_arr[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        buffer_elements[buffer_arr[ord(arr[i][k]) - ord('a')] - 1] = arr[i]
        buffer_arr[ord(arr[i][k]) - ord('a')] -= 1
    for i in range(len(arr)):
        arr[i] = buffer_elements[i]
        #arr = copy.deepcopy(buffer_elements)
 
n, m, k = map(int, file_input.readline().split())
arr = [file_input.readline()[:m] for _ in range(n)]
for i in range(m - 1, m - k - 1, -1):
    get_radix_kth(arr, m, i)
for i in range(n):
    print(arr[i], file=file_output)
file_output.close()
