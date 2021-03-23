import asyncio

future = None

async def unblock_future():
    global future
    future.set_result(True)
    print("Unblock future")

async def main():
    global future
    loop = asyncio.get_event_loop()
    asyncio.create_task(unblock_future())

    future = loop.create_future()
    
    print("Before is blocked")
    await future
    print("Before is unblocked")

if __name__ == "__main__":
    print("Begin")
    asyncio.run(main())
    print("Complete")
