import threading
threading.stack_size(3 * 67108864)

def main():
    n = int(input())
    data = list(map(int, input().split())) 
    # [list] subseq: length of subsequence ended on i-th elem
    subseq, sequence = [1] * n, [-1] * n
    for i in range(n):
        for j in range(i):
            if subseq[j] + 1 > subseq[i] and data[i] > data[j]:
                subseq[i] = subseq[j] + 1
                sequence[i] = j
    #result sequence (seq_len, index) <- (max(subseq), index(seq_len))
    seq_len = max(subseq)
    index = subseq.index(seq_len)
    ans = []
    while index != -1:
        ans.append(data[index])
        index = sequence[index]
    print(seq_len)
    print(*ans[::-1])

thread = threading.Thread(target=main)
thread.start()