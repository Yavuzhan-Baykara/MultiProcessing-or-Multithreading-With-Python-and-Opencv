from concurrent.futures import thread
from threading import Thread
from time import sleep, perf_counter
from tracemalloc import start

def task(inp:str= None):
    print(f"Starting task {inp}...")
    sleep(.1/200)
    print("Done...")

#-----------------------------------------------------------------------------------
start_time = perf_counter() 
task(1)
close_time = perf_counter()
print(f"Threadless performance time: {(close_time - start_time): 0.4f}")
#-----------------------------------------------------------------------------------
start_time_thread = perf_counter() 
thread1 = Thread(target= task(2))
thread1.start()
thread1.join()
close_time_thread = perf_counter() 
print(f"Thread performance time: {(close_time_thread - start_time_thread): 0.4f}")
#-----------------------------------------------------------------------------------
def task2():
    for _ in range(10):
        task(3)

start_time_thread_loop = perf_counter() 
thrd = Thread(target= task2)
thrd.start()
thrd.join()
close_time_thread_loop = perf_counter() 
print(f"Thread loop performance time: {(close_time_thread_loop - start_time_thread_loop): 0.4f}")