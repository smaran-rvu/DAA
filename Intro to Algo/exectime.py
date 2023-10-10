import time

start_time = 0
def start(): 
    global start_time
    start_time = time.time()

def end():
    print(f'\nThe time of execution of the program is {time.time() - start_time}')