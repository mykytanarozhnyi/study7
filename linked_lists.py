class Node:

    def __init__(self, _id, value):
        self.id = _id
        self.value = value
        self.next = None

    def __str__(self):
        return f"Node {self.id}: value {self.value}"
class LinkedList:

    def __init__(self):
        self.head = None

    def __len__(self):
        counter = 0
        current = self.head
        while current:
            counter += 1
            current = current.next
        return counter

    def add_node(self, value):
        _id = len(self) + 1
        if not self.head:
            self.head = Node(_id,value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(_id,value)
    def print_nodes(self):
        current = self.head
        while current:
            print(current)
            current = current.next

if __name__ == "__main__":
    node1 = Node(1,5)
    container = LinkedList()
    container.add_node(43)
    container.add_node(50)
    container.add_node(30)
    container.print_nodes()

    for node in container:
        print(node)
