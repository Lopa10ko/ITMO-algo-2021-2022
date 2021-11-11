file_input = open('garland.in', 'r')
file_output = open('garland.out', 'w')
 
#binary left search for sorted data
def binsearch(quantity, first):
    left, right = 0, first
    only_one_on_ground = False
    height = 0
    while right > left + 0.005 / (quantity - 1):
        mid = (left + right) / 2
        lamp_minus = first
        lamp_current = mid
        if lamp_current >= 0:
            not_touching_ground = True
        else:
            not_touching_ground = False
        for i in range(2, n):
            lamp_plus = 2 * lamp_current - lamp_minus + 2
            if lamp_plus < 0:
                 not_touching_ground = False
                 break
            lamp_minus, lamp_current = lamp_current, lamp_plus
        if not_touching_ground:
            right = mid
            height = lamp_current
        else:
            left = mid
    return height
     
n, A = map(float, file_input.readline().split())
n = int(n)
print(binsearch(n, A), file=file_output)
 
file_output.close()
