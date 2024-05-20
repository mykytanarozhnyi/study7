import math
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_decorator(debug=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
        # запам'ятовує час початку виконання задекорованої функції
            start_time = time.time()
            if debug:
                logger.info(f"Execution started at {start_time}")
            result = func(*args, **kwargs)
            end_time = time.time()
            if debug:
                logger.info(f"Execution ended at {end_time}")
            logger.info(f"Execution took {end_time - start_time}")
            return result
        return wrapper
    return decorator

@log_decorator(debug=True)
def gcd_classic(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return m

@log_decorator(debug=True)
def gcd_optimised(a, b):
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    return b

@log_decorator(debug=True)
def math_gcd(a,b):
    math.gcd(a,b)
    result = math.gcd(a,b)
    return result




if __name__ == "__main__":
    print(gcd_classic(999_999, 2))
    print("=============")
    print(gcd_optimised(999_999, 2))
    print(math_gcd(999_999,2))

