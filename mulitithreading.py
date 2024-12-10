import threading

# A shared variable
counter = 0

# A lock to synchronize access to the shared variable
lock = threading.Lock()

# Function to be executed by each thread
def increment():
    global counter

    for _ in range(100000):
        # Acquire the lock
        lock.acquire()
        
        try:
            # Critical section
            counter += 1
        finally:
            # Release the lock
            lock.release()

# Create multiple threads
threads = []
for _ in range(5):
    thread = threading.Thread(target=increment)
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Print the final value of the counter
print("Counter:", counter)