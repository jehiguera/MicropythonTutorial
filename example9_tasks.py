import uasyncio as asyncio
from machine import Timer

tsf = asyncio.ThreadSafeFlag()

def cb(_):
    tsf.set()

async def foo():
    while True:
        await tsf.wait()
        # Could set an Event here to trigger multiple tasks
        print('Triggered')

t = Timer(-1, period=2000, callback=cb)

asyncio.run(foo())