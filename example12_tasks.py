import uasyncio as asyncio
class AsyncIterable:
    def __init__(self):
        self.data = (1, 2, 3, 4, 5)
        self.index = 0

    def __aiter__(self):  # See note below
        return self

    async def __anext__(self):
        data = await self.fetch_data()
        if data:
            return data
        else:
            raise StopAsyncIteration

    async def fetch_data(self):
        await asyncio.sleep(0.1)  # Other tasks get to run
        if self.index >= len(self.data):
            return None
        x = self.data[self.index]
        self.index += 1
        return x

async def run():
    ai = AsyncIterable()
    async for x in ai:
        print(x)
asyncio.run(run())