import threading
import time
import random
from Semaphore import Semaphore


class DiningPhilosophersProblem:
    def __init__(self, num_philosophers):
        self.chopsticks = [Semaphore(1) for _ in range(num_philosophers)]
        self.status = ["holding chopstick [X]" for _ in range(num_philosophers)]
        self.num_philosophers = num_philosophers
  

    def eat(self, philosopher_id):
        left_chopstick = philosopher_id 
        right_chopstick = (philosopher_id + 1) % self.num_philosophers

        while True:
            time.sleep(random.uniform(1,3)) # thinking
            self.status[philosopher_id] = "holding chopstick [{}]".format(left_chopstick)
            self.chopsticks[left_chopstick].wait()
            self.status[philosopher_id] = "holding chopstick [{}]".format(right_chopstick)
            self.chopsticks[right_chopstick].wait()

            self.status[left_chopstick] = "eating"
            time.sleep(random.uniform(1,3)) # eating right now

            #Stop eating
            self.chopsticks[left_chopstick].signal()
            self.chopsticks[right_chopstick].signal()
    #print out the result here
    def print_status(self):
        while True:
            print("Philosophers status:")
            for i, status in enumerate(self.status):
      
                print(f"[Philosopher {i}: {status}]")
            #delay 5s
            time.sleep(5)