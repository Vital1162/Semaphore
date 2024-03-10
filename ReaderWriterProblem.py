from Semaphore import Semaphore
import threading
import time
import random
class ReaderWriterProblem:
    def __init__(self):
        self.mutex = Semaphore(1) #a binary semaphore -> Đảm bảo tính loại trừ
        self.resource = Semaphore(1)
        self.read_count = 0 # bao nhiêu processes đang đọc

    
    def reader(self):
        while True:
            self.mutex.wait() #take a key to read
            self.read_count += 1 # bây giờ reader tăng lên 1
            if self.read_count == 1:
                self.resource.wait() # đảm bảo không reader có thể vào CS
            self.mutex.signal() # người đọc khác có thể vào khi reader hiện tại khác đang ở CS

            print("Reading data")

            self.mutex.wait()
            self.read_count -= 1 #Reader muốn rời đi
            if self.read_count == 0: # nếu không có reader nào CS
                self.resource.signal() # điều này cho phép writer có thể vào CS
            self.mutex.signal() # Reader rời khỏi CS
            time.sleep(random.uniform(0.1, 0.5))

    def writer(self):
        while True:
            self.resource.wait()
            print("Writing data")
            self.resource.signal()
            time.sleep(random.uniform(0.1, 0.5))