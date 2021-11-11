file_input = open('priorityqueue.in', 'r')
file_output = open('priorityqueue.out', 'w')
import copy
 
 
def sift_up(arr, length):
        while length != 0 and arr[length][0] < arr[(length - 1) // 2][0]:
              arr[length], arr[(length - 1) // 2] = arr[(length - 1) // 2], arr[length]
              length = (length - 1) // 2
        return arr
 
def sift_down(arr, param):
        left, right, tmp = 0, 0, 0
        #print('----')
        #print(*arr)
        while len(arr) > 2 * param + 1:
            left = 2 * param + 1
            right, tmp = left + 1, left
            if right < len(arr):
                if arr[right][0] < arr[left][0]: tmp = right
            if arr[param][0] <= arr[tmp][0]: break
            arr[param], arr[tmp] = arr[tmp], arr[param]
            param = tmp
        #print(*arr)
        return arr
     
class ImplementedQueue(object):
    def __init__(self):
        self.que = []
 
    def __str__(self):
        return ''.join([str(x) for x in self.que])
    
    def push_element(self, element, cnt):
        self.que.append([element, cnt])
        self.que = sift_up(self.que, len(self.que) - 1)
        #print(*self.que)
 
    def decrease_key(self, index, value):
        for i in range(len(self.que)):
            if self.que[i][1] == index:
                self.que[i][0] = value
                sift_up(self.que, i)
                break
         
    def get_min(self):
        try:
            min_element = self.que[0][0]
            self.que[0] = self.que[len(self.que) - 1]
            self.que.pop(-1)
            sift_down(self.que, 0)
            print(min_element, file=file_output) 
        except IndexError:
            return
 
 
if __name__ == '__main__':
    cnt, arr = 1, ImplementedQueue()
    current, new_current = file_input.readline().split(), ''
    while current[0] in ['push', 'extract-min', 'decrease-key']:
        if current[0] == 'push':
            arr.push_element(int(current[1]), cnt)
        elif current[0] == 'extract-min':
            if not arr.que:
                print('*', file=file_output)
            else:
                arr.get_min()
        else:
            arr.decrease_key(int(current[1]), int(current[2]))
        cnt += 1
        new_current = file_input.readline()
        if new_current:
            current = new_current.split()
        else:
            break
 
file_output.close()
