import threading

class Semaphore:
    """

    """
    def __init__(self, initial):
        """
        lock: đảm bảo rằng chỉ một thread có thể thực hiện một
        phần của mã tại một thời điểm.
        value
        """
        self.lock = threading.Condition(threading.Lock())
        self.value = initial

    def signal(self):
        with self.lock:
            self.value += 1
            self.lock.notify()#thông báo thêm vào hàng đợi
    
    def wait(self):
        with self.lock:
            while self.value == 0:
                self.lock.wait()
            self.value -= 1