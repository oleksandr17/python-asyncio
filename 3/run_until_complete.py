import asyncio

async def child():
    print("Child")

async def main():
    print("Begin")
    asyncio.create_task(child())
    print("Before sleep")
    await asyncio.sleep(3)
    print("End")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
