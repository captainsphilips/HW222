import time 
def timeme(func):
    def wrapper(): 
        start = time.time() 
        func()
        end = time.time() 
        print(f"Total time {end - start}") 
    return wrapper