import threading
import time

def prepare_coffee(type_, wait_time ):
    print(f"{type_} coffee: brewing...")
    time.sleep(wait_time)
    print(f"{type_} coffee: Ready.")


t1 = threading.Thread(target=prepare_coffee, args=("Black", 2))
t2 = threading.Thread(target=prepare_coffee, args=("Mocha", 3))

t1.start()
t2.start()
t1.join()
t2.join()