file_input, file_output = open('input.txt', 'r'), open('output.txt','w')

n, m = map(int, file_input.readline().split())
contig_lst = [0 for _ in range(n)]
for _ in range(m):
    current = list(map(int, file_input.readline().split()))
    contig_lst[current[0] - 1] += 1
    contig_lst[current[1] - 1] += 1
print(*contig_lst, file=file_output)

file_output.close()