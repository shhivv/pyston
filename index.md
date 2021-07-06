## Pyston

<br>

### Basic implementation
```py
from pyston import PystonClient
import asyncio

async def main():
    client = PystonClient()
    output = await client.execute("python","print('Hello World')")
    print(output)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```