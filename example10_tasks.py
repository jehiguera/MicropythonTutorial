import uasyncio as asyncio

class Foo():
    def __iter__(self):
        for n in range(5):
            print('__iter__ called')
            yield from asyncio.sleep(1) # Other tasks get scheduled here
        return 42

async def bar():
    foo = Foo()  # Foo is an awaitable class
    print('waiting for foo')
    res = await foo  # Retrieve result
    print('done', res)

asyncio.run(bar())