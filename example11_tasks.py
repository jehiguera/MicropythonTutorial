up = False  # Running under MicroPython?
try:
    import uasyncio as asyncio
    up = True  # Or can use sys.implementation.name
except ImportError:
    import asyncio

async def times_two(n):  # Coro to await
    await asyncio.sleep(1)
    return 2 * n

class Foo():
    def __await__(self):
        res = 1
        for n in range(5):
            print('__await__ called')
            if up:  # MicroPython
                res = yield from times_two(res)
            else:  # CPython
                res = yield from times_two(res).__await__()
        return res

    __iter__ = __await__

async def bar():
    foo = Foo()  # foo is awaitable
    print('waiting for foo')
    res = await foo  # Retrieve value
    print('done', res)

asyncio.run(bar())