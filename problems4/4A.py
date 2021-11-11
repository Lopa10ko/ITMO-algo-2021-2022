file_input = open('stack.in', 'r')
file_output = open('stack.out', 'w')
 
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
        try:
            if validate_stack(self.top):
                return
            else:
                self.top -= 1
                return self.stack[self.top + 1]             
        except IndexError:
            return
 
 
if __name__ == '__main__':
    arr = ImplementedStack()
    for i in range(int(file_input.readline())):
        current= file_input.readline().split()
        if current[0] == '+':
            arr.push_value(int(current[1]))
        else:
            print(arr.pop_value(), file=file_output)
         
file_output.close()
