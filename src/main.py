import os
import asyncio
import pybotters
from rich import print
from dotenv import load_dotenv
load_dotenv()

api = {
    'ftx': [os.getenv('FTX_API_KEY'), os.getenv('FTX_API_SECRET')],
}

parameters = {
  "market": "XRP/USD",
  "side": "buy",
  "price": None,
  "type": "market",
  "size": 1,
  "reduceOnly": False
}

async def main():
    async with pybotters.Client(apis=api, base_url='https://ftx.com/api') as client:
        resp = await client.post('/orders', data=parameters)
        print(api)
        print(resp)
        return resp

if __name__ == '__main__':
    asyncio.run(main())