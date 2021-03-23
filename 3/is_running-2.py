import asyncio

async def sum(a, b):
    return a + b

async def main():
    s = await sum(1, 2)
    print(f"sum = {s}")
    print(f"Is loop running = {asyncio.get_event_loop().is_running()}")

if __name__ == "__main__":
    print("Begin")
    asyncio.run(main())
    print("Complete")