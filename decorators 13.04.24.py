from math import pi
#def pop_b(data):
#    data.pop("b")
#    return data

#def get_data(callback_func):
#    data = {"a":1,"b":2}
#    return callback_func(data)

#if __name__ == "__main__":
#    get_data(print)
#    data = get_data(pop_b)
#    print(data)

#def volume(r=3,h=1):
#    return r * h * pi**2

#if __name__ == "__main__":
#    volume(h=10)
#    volume(h=19)
#    volume(h=8)
#    volume(r=5,h=9)
def catch_error(print_message):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except KeyError:
                if print_message:("Error happend")
#                else:
#                    pass
#            return wrapper
#        return inner

#import time
#import logging

#logging.basicConfig(...)
#logger = logging.getLogger(__name__)

def first_decorator(func):
    def wrapper():
        try:
            func()
            print("wake up")
        except KeyError:
            pass
    return wrapper

def second_decorator(func):
    def wrapper():
        print("Second in")
        func()
        print("Second out")
    return wrapper

def log_decorator(func):
    def wrapper():
        # запам'ятовує час початку виконання задекорованої функції
        start_time = ...
        if debug:
            logger.info(f"Execution started at {start_time}")
        func()
        end_time = ...
        if debug:
            logger.info(f"Execution ended at {end_time}")
        logger.info(f"Execution took {end_time - start_time}")
    return wrapper

# @second_decorator
# @first_decorator
@log_decorator(debug=False)
def long_function():
    time.sleep(5)
    print("Inside the function")
    raise KeyError

@log_decorator(debug=True)
def other_function():
    time.sleep(2)
    print("Another function")

# long_function = first_decorator(long_function)

if __name__ == "__main__":
    long_function()