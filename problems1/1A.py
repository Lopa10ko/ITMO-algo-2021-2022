file_input, file_output = open('aplusb.in'), open('aplusb.out', 'w')
a, b = map(int, file_input.readline().split())
print(a + b, file=file_output)
file_output.close()
