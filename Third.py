import First
import Second
import time

def comparison():
    filepath = r'C:\Users\klodb\Documents\Учеба\Лабы\Инфа\3\schedule.txt'
    output = r'C:\Users\klodb\Documents\Учеба\Лабы\Инфа\3\new2.txt'
    tic = time.perf_counter()
    First.conversion(filepath, output)
    toc = time.perf_counter()
    print(f"Вычисление First заняло {toc - tic:0.4f} секунд")
    tic = time.perf_counter()
    Second.conversion(filepath, output)
    toc = time.perf_counter()
    print(f"Вычисление Second заняло {toc - tic:0.4f} секунд")

comparison()