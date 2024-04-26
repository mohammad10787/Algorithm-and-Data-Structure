# # First way to implement queue is to use list:
# wmt_stock_price = []
#
# wmt_stock_price.insert(0,131.10)
# wmt_stock_price.insert(0,132.12)
# wmt_stock_price.insert(0,135)
#
# # But lists have their own issues like in dynamic arrays
#
# from collections import deque
# q = deque()
# q.appendleft(5)
# q.appendleft(8)
# q.appendleft(10)

# Like before we can define a class for Queue
from collections import deque
import time

class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        print(self.buffer.pop())

    def is_empty(self):
        return len(self.buffer)

    def size(self):
        return len(self.buffer)

if __name__ == "__main__":
    # print(wmt_stock_price.pop())
    # print(q.pop())
    pq = Queue()

    pq.enqueue({
        'company': 'Wall Mart',
        'timestep': '15 apr, 11:01 AM',
        'price': 131.10
    })

    pq.enqueue({
        'company': 'Wall Mart',
        'timestep': '15 apr, 11:02 AM',
        'price': 132
    })

    pq.enqueue({
        'company': 'Wall Mart',
        'timestep': '15 apr, 11:03 AM',
        'price': 135.10
    })

    pq.dequeue()
    print(pq.buffer)
    print(pq.size())