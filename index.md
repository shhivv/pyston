## Pyston

This is the documentation for Pyston, a library for Python to aid in creating applications that utilise the Piston API.

 
## Installation

Pyston can be installed using the following command

```py
pip install pystonwrapper
```

## Basic implementation

The simplest way to run a line of code in Piston

```py
from pyston import PystonClient
import asyncio

async  def  main():

	client =  PystonClient()
	output =  await client.execute("python","print('Hello World')")
	print(output)
	#Hello World

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

  

## PystonClient

The PystonClient class is used to create an session to communicate with the API


### Parametres

- `api_key : Optional[str]`

### Methods

-  get_runtimes()
	Used to fetch the runtimes provided by the Piston API
	`client.get_runtimes()`