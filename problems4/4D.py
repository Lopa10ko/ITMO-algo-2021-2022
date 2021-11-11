file_input = open('postfix.in', 'r')
file_output = open('postfix.out', 'w')
 
 
def validate_stack(top_index):
        return True if (top_index == -1) else False
     
class ImplementedStack(object):
    def __init__(self):
        self.stack = []
        self.top = -1
    
    def push_value(self, value):
        self.top += 1
        self.stack += ['']
        self.stack[self.top] = value
         
    def pop_value(self):
        if validate_stack(self.top):
            return
        else:
            self.top -= 1
            return self.stack[self.top + 1]             
 
 
if __name__ == '__main__':    
    current = file_input.readline().split()
    arr = ImplementedStack()
    tmp = 0
    for element in current:
        if element not in ['+', '-', '*']:
            arr.push_value(element)
        elif element == '+':
            arr.push_value(int(arr.pop_value()) + int(arr.pop_value()))
        elif element == '-':
            arr.push_value(((- 1) * int(arr.pop_value())) + int(arr.pop_value()))    
        elif element == '*':    
            arr.push_value(int(arr.pop_value()) * int(arr.pop_value()))
print(arr.pop_value(), file=file_output)
 
file_output.close()
