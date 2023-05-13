import time
from contextlib import contextmanager
import gc

def fibonacciIterative(num):
    li = [0, 1]
    for i in range(num):
        i += 2
        li.append(li[i-2] + li[i -1])

    return li[num]

def fibonacciRecursive(num):
    if num < 2:
        return num
    
    return fibonacciRecursive(num - 1) + fibonacciRecursive(num - 2)

@contextmanager
def timer(lable:str):
    start: float = time.perf_counter()
    try:
        yield
    finally:
        end: float = time.perf_counter()
        print(f'{lable}: {end - start:3f} secs')

for i in range(1):
    # gc.collect()
    # with timer("Forloop"):
    #     result = fibonacciIterative(8)
    with timer("Recursive"):
        result = fibonacciRecursive(50)
        print(result)
    time.sleep(1)