def simple_gen():
    sequence = ["apple", "amaze", "shit", "yes", "no", "thx"]
    index = 0
    while index < len(sequence):
        yield sequence[index]
        index += 2
def sequential_yield():
    sequence = [1,2,3,4,5]
    yield sequence[0]
    yield sequence[1]
    yield sequence[2]
    yield sequence[3]
    yield sequence[4]
    yield sequence[5]

if __name__ == '__main__':
    element = (x for x in [1,2,3]) #generator expression
    print(element)
    """def element():
        for x in [1,2,3]:
            yield x"""
    print(simple_gen())
    for val in simple_gen():
        print(val)