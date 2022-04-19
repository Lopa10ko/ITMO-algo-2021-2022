from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(3 * 67108864)

def main():
    file_input, file_output = open("selectw.in", 'r'), open("selectw.out", 'w')
    def cover(vertex):
        nonlocal set_tree, weight
        if set_tree[vertex]: return set_tree[vertex]
        leaf_len, deep_leaf_len = 0, 0
        for ver in leaf[vertex]: leaf_len += cover(ver)
        for ver in deep_leaf[vertex]: deep_leaf_len += cover(ver)
        set_tree[vertex] = max(leaf_len, deep_leaf_len + weight[vertex])
        return set_tree[vertex]
    n, root = int(file_input.readline()), 0
    set_tree, weight = [0] * (n + 1), [0] * (n + 1)
    leaf, deep_leaf = [[] for _ in range(n + 1)], [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        elem = list(map(int, file_input.readline().split()))
        leaf[elem[0]].append(i)
        weight[i] = elem[1]
        if elem[0] == 0: root = i
    for i in range(n + 1):
        for elem in leaf[i]:
            for deep_elem in leaf[elem]: deep_leaf[i].append(deep_elem)
    print(cover(root), file=file_output)
    file_output.close()

thread = threading.Thread(target=main)
thread.start()