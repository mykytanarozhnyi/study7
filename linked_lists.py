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

    def find_node_by_id(self, _id):
        current = self.head
        while current:
            if current.id == _id:
                return current
            current = current.next
        return None

    def remove_last_node(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def __iter__(self):
        self._current = self.head
        return self

    def __next__(self):
        if self._current:
            current_node = self._current
            self._current = self._current.next
            return current_node
        else:
            raise StopIteration






if __name__ == "__main__":
    node1 = Node(1,5)
    container = LinkedList()
    container.add_node(43)
    container.add_node(50)
    container.add_node(30)
    container.print_nodes()

    for node in container:
        print(node)

    print("\nFinding node with id:")
    node = container.find_node_by_id(3)
    print(node if node else "Node not found")

    print("\nRemoving last node:")
    container.remove_last_node()
    container.print_nodes()
