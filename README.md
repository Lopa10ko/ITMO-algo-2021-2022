# ITMO-algo-2021-2022

## Labs:

Lab1 (Знакомство с проверяющей системой PCMS):
* [A - A + B](https://github.com/Lopa10ko/ITMO-algo-2021-2022/blob/main/problems1/1A.py)
* [B - A + B * B](https://github.com/Lopa10ko/ITMO-algo-2021-2022/blob/main/problems1/1B.py)
* [C - Простая сортировка](https://github.com/Lopa10ko/ITMO-algo-2021-2022/blob/main/problems1/1C.py)
* [D - Знакомство с жителями Сортленда](https://github.com/Lopa10ko/ITMO-algo-2021-2022/blob/main/problems1/1D.py)
* [E - Черепашка](https://github.com/Lopa10ko/ITMO-algo-2021-2022/blob/main/problems1/1E.py)

Lab2 (Сортировка слиянием и быстрая сортировка):
* [A - Сортировка](https://github.com/Lopa10ko/ITMO-algo-2021-2022/blob/main/problems2/2A.py)
* [B - Соревнования по бегу](https://github.com/Lopa10ko/ITMO-algo-2021-2022/blob/main/problems2/2B.py)
* [C - Число инверсий](https://github.com/Lopa10ko/ITMO-algo-2021-2022/blob/main/problems2/2C.py)
* [D - Анти-Quicksort](https://github.com/Lopa10ko/ITMO-algo-2021-2022/blob/main/problems2/2D.py)
* [E - K-ая порядковая статистика](https://github.com/Lopa10ko/ITMO-algo-2021-2022/blob/main/problems2/2E.py)
 
* Lab3 (Пирамидальная сортировка и цифровая сортировка):
* [A - Пирамида ли?](https://github.com/Lopa10ko/ITMO-algo-2021-2022/blob/main/problems3/3A.py)
* [B - Пирамидальная сортировка](https://github.com/Lopa10ko/ITMO-algo-2021-2022/blob/main/problems3/3B.py)
* [C - Цифровая сортировка](https://github.com/Lopa10ko/ITMO-algo-2021-2022/blob/main/problems3/3C.py)
* [D - Приоритетная очередь](https://github.com/Lopa10ko/ITMO-algo-2021-2022/blob/main/problems3/3D.py)

* Lab4 (Стек, очередь и бинпоиск):
* [A - Стек](https://github.com/Lopa10ko/ITMO-algo-2021-2022/blob/main/problems4/4A.py)
* [B - Очередь](https://github.com/Lopa10ko/ITMO-algo-2021-2022/blob/main/problems4/4B.py)
* [C - Правильная скобочная последовательность](https://github.com/Lopa10ko/ITMO-algo-2021-2022/blob/main/problems4/4C.py)
* [D - Постфиксная запись](https://github.com/Lopa10ko/ITMO-algo-2021-2022/blob/main/problems4/4D.py)
* [E - Двоичный поиск](https://github.com/Lopa10ko/ITMO-algo-2021-2022/blob/main/problems4/4E.py)
* [F - Гирлянда](https://github.com/Lopa10ko/ITMO-algo-2021-2022/blob/main/problems4/4F.py)

## Facts:
> Bad programmers worry about the code. Good programmers worry about data structures and their relationships. (c) Linus Torvalds

## Python threading

```py
from sys import setrecursionlimit
import threading
setrecursionlimit(10 ** 9)
threading.stack_size(67108864)
 
def main():
    ...
     
thread = threading.Thread(target=main)
thread.start()
```
