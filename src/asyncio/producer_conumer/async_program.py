import asyncio
import datetime
import random

import colorama


def main():

    loop = asyncio.get_event_loop()

    t0 = datetime.datetime.now()
    print(colorama.Fore.WHITE + "App started.", flush=True)

    # data structure- first in first out
    data = asyncio.Queue()

    # coroutines
    task1 = loop.create_task(generate_data(20, data))
    task2 = loop.create_task(generate_data(20, data))
    task3 = loop.create_task(process_data(40, data))

    final_task = asyncio.gather(task1, task2, task3)

    loop.run_until_complete(final_task)

    dt = datetime.datetime.now() - t0

    print(
        colorama.Fore.WHITE
        + f"App exiting, total time: {dt.total_seconds():,.2f} sec.",
        flush=True,
    )


async def generate_data(num: int, data: asyncio.Queue):
    for idx in range(1, num + 1):
        item = idx * idx

        # run until `item` then wait here...
        await data.put((item, datetime.datetime.now()))

        # ... then do this
        print(colorama.Fore.YELLOW + f" -- generated item {idx}", flush=True)

        # then wait until done sleeping then start loop over
        await asyncio.sleep(random.random() + 0.5)


async def process_data(num: int, data: asyncio.Queue):
    processed = 0
    while processed < num:
        # call coroutine
        item = await data.get()
        processed += 1
        value = item[0]
        t = item[1]
        dt = datetime.datetime.now() - t

        print(
            colorama.Fore.CYAN
            + f" +++ Processed value {value} after {dt.total_seconds():,.2f} sec.",
            flush=True,
        )
        await asyncio.sleep(0.5)


if __name__ == "__main__":
    main()
