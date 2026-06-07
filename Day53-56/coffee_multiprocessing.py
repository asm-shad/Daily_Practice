from multiprocessing import Process
import time

def brew_coffee(name):
    print(f"Start of {name} Coffee brewing.")
    time.sleep(3)
    print(f"End of {name} Coffee brewing.")

if __name__ == "__main__":
    coffee_makers = [
        Process(target=brew_coffee, args=(f"Coffee Maker #{i+1}", ))
        for i in range(3)
    ]

    # Start all processes
    for p in coffee_makers:
        p.start()

    # Wait for all to complete
    for p in coffee_makers:
        p.join()

    print("All Coffee served!!!")