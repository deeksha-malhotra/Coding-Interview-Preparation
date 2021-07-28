
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next

            cur.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        if self.head == None:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def remove(self, key):

        # if key == head node
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next

            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur_node = self.head
            prev_node = None
            # not equal to head node
            while cur_node.next != self.head:
                prev_node = cur_node
                cur_node = cur_node.next
                if cur_node.data == key:
                    prev_node.next = cur_node.next
                    cur_node = cur_node.next

    def print_list(self):
        cur = self.head

        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break


c = CircularLinkedList()
c.append(1)
c.append(2)
c.append(3)
c.append(4)

# c.remove(1)
# c.remove(3)
c.remove(4)
c.remove(8)

# c.remove(1)
c.print_list()
