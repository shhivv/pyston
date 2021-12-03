# Pyston
An asynchronous API wrapper for the <a href="https://github.com/engineer-man/piston">Piston API</a>.


## Installation
```
pip install aiopyston
```

## Basic implementation
```py
from pyston import PystonClient, File
import asyncio


async def main():
    client = PystonClient()
    output = await client.execute("python", [File("print('Hello world')")])
    print(output)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
### Check out the <a href="https://aiopyston.readthedocs.io/">documentation</a> for more information

