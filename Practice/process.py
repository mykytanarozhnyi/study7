from multiprocessing import Process

def sleep_and_print(num):
    time.sleep(num/10)
    print(num)

def main():
    for i in range(10):
        process = Process(target=sleep_and_print, args=(i))
        process.start()
        process.join()

if __name__ == "__main__":
    main()
