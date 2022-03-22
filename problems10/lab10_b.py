file_input, file_output = open("spantree.in", "r"), open("spantree.out", "w")

n = int(file_input.readline())
max_verge = float("inf")
#all_weights: [(marked/not marked), [list of weigts between current vertex and others]]
all_weights = [[None, []] for _ in range(n)]
vertex_xy = [list(map(int, file_input.readline().split())) for _ in range(n)]
weight_lst = [0] + [max_verge for _ in range(1, n)]
for i in range(n):
    point1 = vertex_xy[i]
    for j in range(n):
        point2 = vertex_xy[j]
        all_weights[i][1].append((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
for _ in range(n):
    current = None
    for j in range(n):
        #if not marked and (is_first_vertex or is_min(list of all weights to one vertex))
        if not all_weights[j][0] and (current is None or weight_lst[j] < weight_lst[current]):
            current = j
    all_weights[current][0] = 1
    for vertex in range(n):
        if not all_weights[vertex][0] and all_weights[current][1][vertex] < weight_lst[vertex] and vertex is not current:
            weight_lst[vertex] = all_weights[current][1][vertex]
print(sum(verge ** 0.5 for verge in weight_lst), file = file_output)

file_output.close()
