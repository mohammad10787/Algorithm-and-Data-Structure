from collections import deque
import time
import threading

class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, orders):
        for order in orders:
            print("Placing order for:", order)
            self.buffer.appendleft(order)
            time.sleep(0.5)

    def dequeue(self):
        time.sleep(1)
        while self.is_empty():
            order = self.buffer.pop()
            print("Now serving:", order)
            time.sleep(2)


    def is_empty(self):
        return len(self.buffer)

    def size(self):
        return len(self.buffer)

if __name__ == "__main__":
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']

    pq = Queue()

    t1 = threading.Thread(target=pq.enqueue, args=(orders,))
    t2 = threading.Thread(target=pq.dequeue)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
