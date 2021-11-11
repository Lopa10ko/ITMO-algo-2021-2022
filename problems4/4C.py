file_input = open('brackets.in', 'r')
file_output = open('brackets.out', 'w')
 
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
        if self.top < 0:
            return 'error'
        else:
            self.top -= 1
            return self.stack[self.top + 1]             
 
 
 
if __name__ == '__main__':    
    current, new_current = file_input.readline(), ''
    while current:
        arr = ImplementedStack()
        ans = 'YES'
        cnt = 0
        for bracket in current:
            if bracket in [')', ']']:
                cnt += 1
                tmp = arr.pop_value()
                if bracket == ')' and tmp != '(' or bracket == ']' and tmp != '[' or tmp == 'error':
                    ans = 'NO'
##                    break
            elif bracket in ['(', '[']:
                cnt -= 1
                arr.push_value(bracket)
            else:
                break                            
        new_current = file_input.readline()
        if cnt != 0:
            ans = 'NO'
        print(ans, file=file_output)
        if new_current:
            current = new_current
        else:
            break
               
file_output.close()
