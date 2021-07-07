## Pyston


##  Basic implementation
The simplest way to run a line of code in Piston
```py
from pyston import PystonClient
import asyncio

async def main():
    client = PystonClient()
    output = await client.execute("python","print('Hello World')")
    print(output)
    #Hello World

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```