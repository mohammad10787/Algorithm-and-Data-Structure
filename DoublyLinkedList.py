class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DLinkedList:
    def __init__(self):
        self.head = None


    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        # #
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr


    def print_forward(self):

        if self.head is None:
            print("Linked List is Empty")

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)


    def print_backward(self):

        if self.head is None:
            print("Linked List is Empty")
            return

        itr = self.get_last_node()
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->' if itr.prev else str(itr.data)
            itr = itr.prev
        print("Linked List in reverse:", llstr)


    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)


    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                node.next.prev = node
                itr.next = node
                break
            count += 1
            itr = itr.next


    def remove_at(self, index):
        if index <0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head

        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                    break
                break
            count += 1
            itr = itr.next



# main excution

if __name__ == '__main__':
    dll = DLinkedList()
    dll.insert_values(["apple", "banana", "pineapple", "watermelon"])
    dll.print_forward()
    dll.print_backward()
    dll.insert_at_begining("avocado")
    dll.print_forward()
    dll.print_backward()
    dll.insert_at_end("Zoolbia")
    dll.print_forward()
    dll.print_backward()
    dll.insert_at(2, "ananas")
    dll.print_forward()
    dll.print_backward()
    dll.remove_at(2)
    dll.print_forward()
    dll.print_backward()



