import aiohttp
import asyncio

async def main():

    async with aiohttp.ClientSession() as session:
        calculation = input('Enter the calculation(example: 1+1) or Q to quit:')
        print(calculation)
        async with session.get('http://0.0.0.0:8080/{calculation}') as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            html = await response.text()
            print("Body:", html[:15])



loop = asyncio.get_event_loop()
loop.run_until_complete(main())