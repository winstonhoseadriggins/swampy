mutex = Semaphore()
x = 0

#thread

mutex.wait()
x = x + 1
mutex.signal()

#     thread

mutex.wait()
x = x + 1
mutex.signal()

