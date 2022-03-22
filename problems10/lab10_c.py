file_input, file_output = open("spantree3.in", "r"), open("spantree3.out", "w")
# lame Kruskal (6 -- WA)
n, m = map(int, file_input.readline().split())
full_span = sorted([tuple(map(int, file_input.readline().split()))
                   for _ in range(m)], key=lambda x: x[2])
span_value, components, marked = 0, {}, set()
for vertex in full_span:
    if any([vertex[0] not in marked,  vertex[1] not in marked]):
        if all([vertex[0] not in marked,  vertex[1] not in marked]):
            components[vertex[0]] = [vertex[0], vertex[1]]
            components[vertex[1]] = components[vertex[0]]
        else:
            if not components.get(vertex[0]):
                components[vertex[1]].append(vertex[0])
                components[vertex[0]] = components[vertex[1]]  # add key
            else:
                components[vertex[0]].append(vertex[1])
                components[vertex[1]] = components[vertex[0]]  # add key
        span_value += vertex[2]
        marked.add(vertex[0])
        marked.add(vertex[1])
for vertex in full_span:
    if vertex[1] not in components[vertex[0]]:
        span_value += vertex[2]
        temp = components[vertex[0]]
        components[vertex[0]] += components[vertex[1]]
        components[vertex[1]] += temp
print(span_value, file=file_output)

file_output.close()