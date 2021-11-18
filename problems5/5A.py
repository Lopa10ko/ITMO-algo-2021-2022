file_input = open("height.in", 'r')
file_output = open("height.out", 'w')
     
##def get_height(bst, parent, current_height, height):
##    if height[0] <= current_height:
##        height[0] = current_height
##    if bst[parent][1] != 0:
##        get_height(bst, bst[parent][1] - 1, current_height + 1, height)
##    if bst[parent][2] != 0:
##        get_height(bst, bst[parent][2] - 1, current_height + 1, height)
      
n = int(file_input.readline())
height = [0] * n
if n == 0:
    print(0, file=file_output)
elif n == 1:
    print(1, file=file_output)
else:
    height[0] = 1
    for i in range(n):
        bst = list(map(int, file_input.readline().split()))
        current = height[i] + 1
        if bst[1] != 0:
            height[bst[1] - 1] = current
        if bst[2] != 0:
            height[bst[2] - 1] = current
    print(max(height), file=file_output)
      
file_output.close()
