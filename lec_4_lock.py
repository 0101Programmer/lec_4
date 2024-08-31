from threading import Thread, Lock

x = 0

lock = Lock()


def thread_task():
    global x
    for i in range(10_000_000):
        lock.acquire()
        x = x + 1
        lock.release()


def main():
    global x
    x = 0
    t1 = Thread(target=thread_task)
    t2 = Thread(target=thread_task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


for i in range(10):
    main()
