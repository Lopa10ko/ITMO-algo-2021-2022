from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(2 * 67108864)

def main():
    file_input, file_output = open('spantree3.in', 'r'), open('spantree3.out','w')

    def get_node(vertex):
        nonlocal component
        return vertex if component[vertex] == vertex else get_node(component[vertex])

    n, m = map(int, file_input.readline().split())
    full_span = []
    for _ in range(m):
        node1, node2, weight = map(int, file_input.readline().split())
        full_span.append([node1 - 1, node2 - 1, weight])
    full_span = sorted(full_span, key=lambda x : x[2])
    component, weights = [x for x in range(n)], [0 for _ in range(n)]
    mst_counter, mst_weight, iterator = 0, 0, 0
    while mst_counter < n - 1:
        node1, node2, weight = full_span[iterator]
        component1, component2 = get_node(node1), get_node(node2)
        if component1 != component2:
            if weights[component1] < weights[component2]:
                component[component1] = component2
            elif weights[component1] > weights[component2]:
                component[component2] = component1
            else:
                component[component2] = component1
                weights[component1] += 1
            mst_counter += 1
            mst_weight += weight
        iterator += 1

    print(mst_weight, file=file_output)
    file_output.close()

thread = threading.Thread(target=main)
thread.start()