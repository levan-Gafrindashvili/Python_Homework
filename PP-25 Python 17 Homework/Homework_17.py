class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        current = self.head

        if current and current.data == data:
            self.head = current.next
            current = None
            return

        prev = None

        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None

    def remove(self, index):
        if self.head is None:
            return
        current = self.head
        if index == 0:
            self.head = current.next
            current = None
            return
        prev = None
        count = 0
        while current and count != index:
            prev = current
            current = current.next
            count += 1
        if current is None:
            return
        prev.next = current.next
        current = None

    def print_list(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("No more")
    
ll = LinkedList()
ll.append(4)
ll.append(3)
ll.append(6)
ll.append(5)
# ll.prepend(2)
# ll.prepend(7)
# ll.delete(2)
# ll.delete(6)

ll.remove(0)
ll.remove(2)

ll.print_list()