class OrderedList:

    def __init__(self):
        self.elements = list()

    def insert(self, value):
        index = 0
        while index < len(self.elements) and self.elements[index] < value:
            index += 1
        self.elements.insert(index, value)



if __name__ == "__main__":
    container = OrderedList()
    container.insert(40)
    container.insert(20)
    container.insert(60)
    container.insert(50)
    container.insert(30)
    container.insert(80)
    print(container.elements)
    print(container.elements) #20, 30 , 40 , 50 , 60

    # як гарантувати щоб новий елемент не зламав впорядкованість нових елементів