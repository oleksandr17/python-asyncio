import asyncio

tasks = []

async def sleep(delay: int):
    try:
        print(f"before delay {delay}")
        await asyncio.sleep(delay)
        print(f"after delay {delay}")
        print(f"remove task with delay {delay}")
        tasks.remove(asyncio.current_task()) # TODO: comment and check
    except asyncio.CancelledError:
        print(f"cancel task with delay {delay}")
    

async def main():
    tasks.append(asyncio.create_task(sleep(2)))
    tasks.append(asyncio.create_task(sleep(70)))
    
    print(f"Wait for {len(tasks)} tasks")
    await asyncio.wait(tasks, timeout=4)
    
    print(f"Cancel {len(tasks)} tasks")
    for task in tasks:
        print(f">>> cancel")
        task.cancel()
    
    await asyncio.gather(*tasks, return_exceptions=True)

    print("Finished waiting")

asyncio.run(main())