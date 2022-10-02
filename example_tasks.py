import uasyncio

# Define Function to be planned
async def text1(text,time):
    while True:
        print(text)
        await uasyncio.sleep(time)

# Delete infinite loop
try:
    import uasyncio
    uasyncio.Loop.stop()
    uasyncio.Task.cancel()
except:
    pass

# Define infinite loop with Tasks
run = uasyncio.new_event_loop()
run.create_task(text1("Log - Taks1 - 2s",2))
run.create_task(text1("Log - Taks2 - 10s",10))
run.run_forever()
run.close()