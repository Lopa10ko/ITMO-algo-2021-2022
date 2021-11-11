file_input, file_output = open('aplusbb.in'), open('aplusbb.out', 'w')
a, b = map(int, file_input.readline().split())
print(a + b ** 2, file=file_output)
file_output.close()
