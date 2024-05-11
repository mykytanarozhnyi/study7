#0(1)
def return_first(iterable):
    return iterable[0]
#0 (log(n))
def binary_search(iterable):
    pass
#0(n)
def double_value(iterable):
    result = list()
    for element in iterable:
        result.append(element * 2 )
    return result
    #return [element * 2 for element in iterable]
def print_double(iterable):
    result = list()
    for element in iterable:
        result.append(element * 2)
        for item in result:
            print(result)
#0(n**2)
def my_sort(iterable):
    for element in iterable:
        for other_element in iterable:
            if element < other_element:
                #swap elements