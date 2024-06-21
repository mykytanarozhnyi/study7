from threads import sleep_and_print, main_with_threads
import time
from process import main
from evclide import log_decorator

#1 варіант


@log_decorator(debug=False)
def finalop():
    return sleep_and_print(5)


finalop()
#now = log_decorator(now)
