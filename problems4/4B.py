file_input = open('queue.in', 'r')
file_output = open('queue.out', 'w')
 
def validate_que(length):
        return True if (length == 0) else False
     
class ImplementedQueue(object):
    def __init__(self):
        self.que = []
        self.head = 0
        self.tail = 0
    
    def push_value(self, value):
        self.que += ['']
        self.que[self.tail] = value
        self.tail += 1
         
    def pop_value(self):
        try:
            if validate_que(self.tail - self.head):
                return
            else:
                self.head += 1
                return self.que[self.head - 1]
                 
        except IndexError:
            return
 
 
if __name__ == '__main__':
    arr = ImplementedQueue()
    for i in range(int(file_input.readline())):
        current= file_input.readline().split()
        if current[0] == '+':
            arr.push_value(int(current[1]))
        else:
            print(arr.pop_value(), file=file_output)
         
file_output.close()
