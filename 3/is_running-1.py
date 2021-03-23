import asyncio

async def sum(a, b):
    return a + b

async def log_loop(loop = None):
    if loop is None:
        loop = asyncio.get_event_loop()
    print(f"Is loop running = {loop.is_running()}")    

loop = asyncio.get_event_loop()

s = loop.run_until_complete(sum(1, 2))
print(f"sum = {s}")
print(f"Is loop running = {loop.is_running()}")

loop.run_until_complete(log_loop())

loop.run_until_complete(log_loop(loop))
