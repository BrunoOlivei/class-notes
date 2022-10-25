import asyncio


async def diz_oi():
    print("Oi")

eventloop = asyncio.get_event_loop()
eventloop.run_until_complete(diz_oi())
eventloop.close()
