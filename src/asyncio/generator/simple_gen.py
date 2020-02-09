from typing import List


def basic_fib(num: int) -> List[int]:
    numbers = []
    current, nxt = 0, 1
    while len(numbers) < num:
        current, nxt = nxt, current + nxt
        numbers.append(current)

    return numbers


def fib():
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, current + nxt
        yield current


result = fib()

for n in result:
    print(n, end=", ")
    if n > 10000:
        break


if __name__ == "__main__":
    print(basic_fib(21))

