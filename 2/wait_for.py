import asyncio
import time

async def eternity():
    # Sleep for one hour
    await asyncio.sleep(3600)

async def main():
    try:
        # Wait for at most 1 second
        await asyncio.wait_for(eternity(), timeout=1.0) # creates a new task for 'eternity'
        # await asyncio.wait({eternity(), eternity()}, timeout=1.0) # creates a new task for 'eternity'
    except asyncio.TimeoutError:
        print('timeout')

asyncio.run(main())