from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(3 * 67108864)

def main(): #Knuth_Morris_Pratt
    file_input, file_output = open("search2.in", 'r'), open("search2.out", 'w')
    def get_prefix(string : str) -> list:
        prefix = [0] + [None for _ in range(len(string) - 1)]
        for i in range(1, len(string)):
            temp = prefix[i - 1]
            while temp > 0 and string[i] != string[temp]:
                temp = prefix[temp - 1]
            if string[i] == string[temp]: temp += 1
            prefix[i] = temp
        return prefix
    pattern, string = file_input.readline().strip(), file_input.readline().strip()
    pattern_len, data_len = len(pattern), len(string)
    prefix = get_prefix(pattern + "$" + string)
    found_indexes = []
    for i in range(pattern_len, pattern_len + data_len + 1):
        if prefix[i] == pattern_len: found_indexes.append(i - pattern_len * 2 + 1)
    print(len(found_indexes), file=file_output)
    print(*found_indexes, file=file_output)
    file_output.close()
thread = threading.Thread(target=main)
thread.start()