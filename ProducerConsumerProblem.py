from Semaphore import Semaphore
import threading
import time
import random

class ProducerConsumerProblem:
    """
        Producer: muốn insert data vào slot rỗng trong bufer, nếu buffer đầy thì
        không thể insert
        Consumer: xóa dữ liệu, nhưng không thể nếu buffer rỗng
        Và cả 2 đều không thể làm việc đồng thời
    """
    def __init__(self):
        self.buffer = [] 
        self.mutex = Semaphore(1) # binary semaphore -> acquire and release
        self.empty = Semaphore(10) # lượng item có thể chứa của buffer
        self.full = Semaphore(0) # số nguyên bình thường 

    def producer(self):
        while True:
            item = random.randint(1, 100)
            self.empty.wait() 
            self.mutex.wait() #acquire lock
            self.buffer.append(item) # thêm dữ liệu vào buffer
            print(f"Produced item {item}")
            self.mutex.signal() # release lock
            self.full.signal() #tăng full khi
            time.sleep(random.uniform(0.1, 0.5))
            

    def consumer(self):
        while True:
            self.full.wait() # chờ tới khi full > 0 rồi giảm full -= 1
            self.mutex.wait() #acqure lock
            item = self.buffer.pop(0) # xóa dữ liệu giống queue
            print(f"Consumed item {item}") 
            self.mutex.signal()# release lock
            self.empty.signal()# tăng empty lên
            time.sleep(random.uniform(0.1, 0.5))