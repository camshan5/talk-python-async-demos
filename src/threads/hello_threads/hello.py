# The Basics of Threads
import time
import threading


def main():
    threads = [
        # Create and start the thread
        threading.Thread(target=greeter, args=("Fitzy", 10), daemon=True),
        threading.Thread(target=greeter, args=("Phoebe", 5), daemon=True),
        threading.Thread(target=greeter, args=("Winnie", 2), daemon=True),
        threading.Thread(target=greeter, args=("Ollie", 11), daemon=True),
    ]

    # list comprehension to start all of the threads in the `threads` list
    [t.start() for t in threads]

    print("\n\tDoing some other work here...")
    print(f"\tThe answer to 2 x 2 is: {2 * 2}\n")
    print("\tEnd of other work\n")

    # Waiting for work to complete
    # Releases final print statement after `greeter` completes its loop
    [t.join(timeout=1) for t in threads]

    print("Done!")


def greeter(name: str, times: int):
    for n in range(0, times):
        print(f"{n}: Hello there {name}\n")
        time.sleep(1)


if __name__ == "__main__":
    main()
