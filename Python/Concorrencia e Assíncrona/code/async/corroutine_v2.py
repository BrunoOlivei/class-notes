import asyncio


async def diz_oi_demorado():
    print("Oi")
    await asyncio.sleep(2)
    print("todos")

eventloop = asyncio.get_event_loop()
eventloop.run_until_complete(diz_oi_demorado())
eventloop.close()
