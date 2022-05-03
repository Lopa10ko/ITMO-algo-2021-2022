from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(3 * 67108864)

def main(): #Knuth_Morris_Pratt
    file_input, file_output = open("prefix.in", 'r'), open("prefix.out", 'w')
    string = file_input.readline().strip()
    prefix = [0] + [None for _ in range(len(string) - 1)]
    for i in range(1, len(string)):
        temp = prefix[i - 1]
        while temp > 0 and string[i] != string[temp]: temp = prefix[temp - 1]
        if string[i] == string[temp]: temp += 1
        prefix[i] = temp
    print(*prefix, file=file_output)
    file_output.close()
thread = threading.Thread(target=main)
thread.start()