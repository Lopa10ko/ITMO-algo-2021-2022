from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(3 * 67108864)
 
def main(): #Knuth_Morris_Pratt
    n = int(input())
    string = input().strip() + "$"
    prefix = [0] + [None for _ in range(len(string) - 1)] + [0]
    for i in range(1, len(string)):
        temp = prefix[i - 1]
        while temp > 0 and string[i] != string[temp]: temp = prefix[temp - 1]
        if string[i] == string[temp]: temp += 1
        prefix[i] = temp
    prefix = [0] + prefix
    kmp = [[0 for _ in range(n)] for _ in range(len(string))]
    for i in range(len(string)):
        elem_i = ord(string[i]) - ord('a')
        for temp in range(n):
            kmp[i][temp] = kmp[prefix[i]][temp] if i > 0 and temp != elem_i else i + (temp == elem_i)
    print(*[' '.join([str(lst) for lst in thing]) for thing in kmp] , sep='\n')

thread = threading.Thread(target=main)
thread.start()