import asyncio
import time

async def cancel_me(v: str):
    try:
        print(f'cancel_me(): try - {v}')
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print(f'cancel_me(): except - {v}')

async def main():
    task1 = asyncio.create_task(cancel_me("1"))
    task2 = asyncio.create_task(cancel_me("2"))

    await asyncio.sleep(1)

    task1.cancel()
    task2.cancel()

    try:
        print("main(): try 1")
        await asyncio.gather(task1, task2)
        print("main(): try 2")
    except asyncio.CancelledError:
        print("main(): except")

asyncio.run(main())