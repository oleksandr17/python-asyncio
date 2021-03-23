import asyncio
import time

async def cancel_me():
    print('cancel_me(): before sleep')

    try:
        # Wait for 1 hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise  # TODO: comment and try
    finally:
        print('cancel_me(): after sleep')

async def main():
    # Create a "cancel_me" Task
    task = asyncio.create_task(cancel_me())

    # Wait for 1 second
    await asyncio.sleep(1)  # TODO: comment and try

    task.cancel()
    try:
        print("main(): before await task")
        await task  # TODO: comment and try
        print("main(): after await task")
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")

asyncio.run(main())