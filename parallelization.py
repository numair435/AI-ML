import time
import threading
import multiprocessing
from multiprocessing import Lock as MP_Lock
from threading import Lock as TH_Lock

def io_task(thread_id, lock):
    with lock:
        print(f"[Thread-{thread_id}] Starting I/O task...")
    time.sleep(2)
    with lock:
        print(f"[Thread-{thread_id}] Finished I/O task.")

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def cpu_task(number, lock):
    result = factorial(number)
    with lock:
        print(f"[Process] factorial({number}) = {result}")

def main():
    print("Starting multithreading and multiprocessing demo...\n")

    thread_lock = TH_Lock()
    threads = []
    for i in range(3):
        t = threading.Thread(target=io_task, args=(i, thread_lock))
        t.start()
        threads.append(t)

    process_lock = MP_Lock()
    numbers = [5, 7, 10]
    processes = []
    for num in numbers:
        p = multiprocessing.Process(target=cpu_task, args=(num, process_lock))
        p.start()
        processes.append(p)

    for t in threads:
        t.join()
    for p in processes:
        p.join()

    print("\nAll tasks completed.")

if __name__ == "__main__":
    main()
