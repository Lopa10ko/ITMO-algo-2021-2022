from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(67108864)
def main():
    file_input = open("quack.in", 'r')
    file_output = open("quack.out", 'w')

    current = file_input.readline().strip()
    actions, marks = [], []

    def move_to(mark):
        for i in range(len(marks)):
            if marks[i][0] == mark:
                return marks[i][1]
        return

    def validate_que(length):
        return True if (length == 0) else False

    class ImplementedQueue():
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

    Quack = ImplementedQueue()
    registers = [0] * 26
    while (current):
        actions.append(current)
        current = file_input.readline().strip()
    for i in range(len(actions)):
        if actions[i][0] == ':':
            marks.append([actions[i][1:], i])
    i, current_action = 0, ''
    a, b, temp = 0, 0, 0
    #print(actions)
    while i < len(actions):
        current_action = actions[i]
        if current_action[0] == 'Q':
            break
        elif current_action[0] == '+':
            Quack.push_value((Quack.pop_value() + Quack.pop_value()) % 65536)

            
        elif current_action[0] == '-':
            Quack.push_value((Quack.pop_value() - Quack.pop_value()) % 65536)
            
        elif current_action[0] == '*':
            Quack.push_value((Quack.pop_value() * Quack.pop_value()) % 65536)
            
        elif current_action[0] == '/':
            a, b = Quack.pop_value(), Quack.pop_value()
            if b == 0:
                Quack.push_value(0)
            else:
                Quack.push_value((a // b) % 65536)
            
        elif current_action[0] == '%':
            a, b = Quack.pop_value(), Quack.pop_value()
            if b == 0:
                Quack.push_value(0)
            else:
                Quack.push_value((a % b) % 65536)
            
        elif current_action[0] == '>':
            registers[ord(current_action[1]) - ord('a')] = Quack.pop_value()
            #print(registers[ord(current_action[1]) - ord('a')])
        elif current_action[0] == '<':
            Quack.push_value(registers[ord(current_action[1]) - ord('a')])

        elif current_action[0] == 'P':
            if len(current_action) > 1:
                temp = registers[ord(current_action[1]) - ord('a')]
            else:
                temp = Quack.pop_value()
            print(temp, file=file_output)
            
        elif current_action[0] == 'C':
            if len(current_action) > 1:
                temp = registers[ord(current_action[1]) - ord('a')]
            else:
                temp = Quack.pop_value()
            print(chr(temp % 256), end='', file=file_output)
            
        elif current_action[0] == ':':
            i += 1
            i -= 1
        elif current_action[0] == 'J':
            i = move_to(actions[i][1:])
            
        elif current_action[0] == 'Z':
            if registers[ord(current_action[1]) - ord('a')] == 0:
                i = move_to(actions[i][2:])

        elif current_action[0] == 'E':
            if registers[ord(current_action[1]) - ord('a')] == registers[ord(current_action[2]) - ord('a')]:
                i = move_to(actions[i][3:])

        elif current_action[0] == 'G':
            if registers[ord(current_action[1]) - ord('a')] > registers[ord(current_action[2]) - ord('a')]:
                i = move_to(actions[i][3:])

        else:
            Quack.push_value(int(current_action))
            #print(current_action)
        i += 1
        #print(registers)

    file_output.close()
thread = threading.Thread(target=main)
thread.start()
