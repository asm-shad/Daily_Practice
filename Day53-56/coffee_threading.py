import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"Taking order for #{i}")
        time.sleep(1)

def brew_coffee():
    for i in range(1,4):
        print(f"Brewing Coffee for #{i}")
        time.sleep(2)

# Create Threads
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_coffee)

order_thread.start()
brew_thread.start()

# Wait for both threads to finish
order_thread.join()
brew_thread.join()

print("All orders taken and coffee brewed!")