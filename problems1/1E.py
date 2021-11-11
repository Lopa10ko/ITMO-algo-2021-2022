file_input = open('turtle.in', 'r')
file_output = open('turtle.out', 'w')

# game board and prizes markup initialization
prizes = []
h, w = map(int, file_input.readline().split())
for i in range(h):
    prizes.append(list(map(int, file_input.readline().split())))
prizes = prizes[::-1]

# prizes borders fill-in
for i in range(1, w):
    prizes[0][i] += prizes[0][i - 1]
for i in range(1, h):
    prizes[i][0] += prizes[i - 1][0]

# prizes body fill-in
for i in range(1, h):
    for j in range(1, w):
        prizes[i][j] += max(prizes[i - 1][j], prizes[i][j - 1])

print(prizes[-1][-1], file=file_output)
file_output.close()
