import asyncio
import time
# async/await

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    return len(what) * delay

async def main():
    print(f"started at {time.strftime('%X')}")

    coro1 = say_after(3, "hello")
    coro2 = say_after(4, "world")
    coro3 = say_after(2, "world")
    coro4 = say_after(5, "world")

    result = await asyncio.gather(coro1, coro2, coro3, coro4)

    print(f"finished at {time.strftime('%X')}")

    print(result)

# asyncio.run(main())
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()