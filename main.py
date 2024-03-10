from DiningPhilosophersProblem import DiningPhilosophersProblem
from ReaderWriterProblem import ReaderWriterProblem
from ProducerConsumerProblem import ProducerConsumerProblem
import threading
import time 
import random


if __name__ == "__main__":
    
    # # Producer-Consumer Problem
    # pc_problem = ProducerConsumerProblem()
    # producer_thread = threading.Thread(target=pc_problem.producer)
    # consumer_thread = threading.Thread(target=pc_problem.consumer)
    # # Start threads
    # producer_thread.start()
    # consumer_thread.start()
    
    # # Join threads
    # producer_thread.join()
    # consumer_thread.join()

    # Reader-Writer Problem
    rw_problem = ReaderWriterProblem()
    reader_thread = threading.Thread(target=rw_problem.reader)
    writer_thread = threading.Thread(target=rw_problem.writer)


    # Start threads
    reader_thread.start()
    writer_thread.start()



    # Join threads
    reader_thread.join()
    writer_thread.join()

    
    # # Dining Philosophers Problem
    # num_philosophers = 5
    # dp_problem = DiningPhilosophersProblem(num_philosophers)
    # philosophers_threads = [threading.Thread(target=dp_problem.eat, args=(i,)) for i in range(num_philosophers)]
    # status_printer_thread = threading.Thread(target=dp_problem.print_status)
    # # Start threads
    # for philosopher_thread in philosophers_threads:
    #     philosopher_thread.start()
    # status_printer_thread.start()
    # # join threads
    # for philosopher_thread in philosophers_threads:
    #     philosopher_thread.join()
    # status_printer_thread.join()