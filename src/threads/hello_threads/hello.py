# The Basics of Threads
import time
import threading


def main():
    t = threading.Thread(target=greeter, args=("Fitzgerald", 10), daemon=True)

    # Start the thread we just created
    t.start()

    print("\n\tDoing some other work here as apart of our main thread...")
    print(f"\tThe answer to 2 x 2 is: {2 * 2}\n")

    # Waiting for work to complete
    # Releases final print statement after `greeter` completes its loop
    t.join()

    print("Done!")


def greeter(name: str, times: int):
    for n in range(0, times):
        print(f"{n}: Hello there {name}\n")
        time.sleep(1)


if __name__ == "__main__":
    main()
