from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(67108864)

def main():
    file_input = open('map.in', 'r')
    file_output = open('map.out', 'w')

    def get_hash(key):
        prime = 239
        hash = 0
        power = 1
        for i in range(len(key)):
            hash += (ord(key[i]) - ord('a') + 1) * power
            power *= prime
        if hash >= 0: return hash % (10 ** 5)
        return ((10 ** 5) - abs(hash) % (10 ** 5)) % (10 ** 5)

    # def validate_que(length):
    #     return True if (length == 0) else False
    # def binsearch(arr, key):
    #     left, right = -1, len(arr)
    #     while right > left + 1:
    #         mid = (left + right) // 2
    #         if arr[mid] < key:
    #             left = mid
    #         else:
    #             right = mid
    #     if right == len(arr):
    #         return "false"
    #     if arr[right] == key:
    #         return "true"
    #     return "false"

    class HashMap():
        def __init__(self):
            self.quantity = 10 ** 5
            self.set = [[] for _ in range(self.quantity)]

        def exists(self, key):
            for pair in self.set[get_hash(key)]:
                if pair[0] == key:
                    return pair[1]
            return "none"

        def insert_value(self, key, value):
            hash = get_hash(key)
            for i in range(int(len(self.set[hash]))):
                if self.set[hash][i][0] == key:
                    self.set[hash][i][1] = value
                    return
            self.set[hash].append([key, value])

        def delete_value(self, key):
            try:
                hash = get_hash(key)
                supremum = int(len(self.set[hash]))
                for i in range(supremum):
                    if self.set[hash][i][0] == key:
                        self.set[hash][i], self.set[hash][supremum - 1] = self.set[hash][supremum - 1], self.set[hash][i]
                        self.set[hash].pop()
                        return
                return
            except IndexError:
                return


    if __name__ == '__main__':
        arr = HashMap()
        current = file_input.readline()
        while current:
            current = current.split()
            if current[0] == 'put':
                arr.insert_value(current[1], current[2])
            elif current[0] == 'delete':
                arr.delete_value(current[1])
            elif current[0] == 'get':
                print(arr.exists(current[1]), file=file_output)
            current = file_input.readline()

    file_output.close()
 
thread = threading.Thread(target=main)
thread.start()
