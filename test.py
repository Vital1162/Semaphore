import threading
import time

class SharedResource:
    def __init__(self):
        self.lock = threading.Lock()  # Tạo một khóa
        self.condition = threading.Condition(self.lock)  # Tạo một điều kiện, sử dụng khóa vừa tạo

    def producer(self):
        with self.lock:
            print("Producer is producing something...")
            time.sleep(2)
            self.condition.notify()  # Thông báo cho các luồng đang chờ
            print("Producer finished producing.")
    
    def consumer(self):
        with self.lock:
            print("Consumer is waiting for production...")
            self.condition.wait(4)  # Đợi cho đến khi được thông báo
            print("Consumer received the production.")

# Tạo một đối tượng chia sẻ
resource = SharedResource()

# Tạo và khởi chạy luồng producer
producer_thread = threading.Thread(target=resource.producer)
producer_thread.start()

# Tạo và khởi chạy luồng consumer
consumer_thread = threading.Thread(target=resource.consumer)
consumer_thread.start()

# Chờ cho cả hai luồng kết thúc
producer_thread.join()
consumer_thread.join()

print("All threads finished.")
