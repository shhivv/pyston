## Pyston

This is the documentation for Pyston, a library for Python to aid in creating applications that utilise the Piston API.

 
## Installation

Pyston can be installed using the following command

```py
pip install aiopyston
```

## Basic implementation

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

### Checkout the <a href="https://ffaanngg.github.io/pyston/#executing-from-a-file">file example</a> to see how to use file objects to execute the code

<br>

## PystonClient

The PystonClient class is used to create an session to communicate with the API


### Initialization Parametres

- `api_key : Optional[str]`

### Methods

-  **get_runtimes()**
	- Used to fetch the runtimes provided by the Piston API
	- Parametres
		- `formatted : Optional[bool] = True`
	- Returns a str or dict
	- Must be awaited


<br>


- **execute()**
	- Used to execute code through the Piston API
	- Parameters
		- `language : str`
		- `code : str`
		- `version : Optional[str] = Latest version`
		- `file_name: Optional[str]`
		- `stdin: Optional[str]`
		- `args: Optional[list]`
		- `compile_timeout: Optional[int] = 10000`
		- `run_timeout: Optional[int] = 3000`
		- `compile_memory_limit: Optional[int] = -1`
		- `run_memory_limit: Optional[int] = -1`

	- Returns a Output object
	- Must be awaited


- **get_aliases()**
	- Used to fetch the aliases of the languages supported by the Piston API
	- Parameters
		- `language : str`

	- Returns a dict
	- Must be awaited


- **get_latest_version()**
	- Used to fetch the latest version of a language supported by the Piston API
	- Parameters
		- `language : str`
		
	- Returns a int
	- Must be awaited


- **get_language_info()**
	- Used to fetch the latest version and the aliases of a languages supported by the Piston API
	- Parameters
		- `language : str`
		
	- Returns a dict
	- Must be awaited


- **languages**
	
	- Property method
	- Returns the languages supported by the Piston API
	- Returns a list
	- Must be awaited
	


	
- **endpoints**
	
	- Property method
	- Returns the endpoints supported by the Piston API
	- Returns a tuple

- **base_url**
	
	- Property method
	- Returns the base url of the API
	- Returns a str


## Output

An output object is returned when a code is exectued

- Attributes
	- language
	- version
	- code
	- signal
	- output
	- stdout
	- stdrr
	
- Property methods
	- success
		- Returns True if the code ran successfully else returns False
	- raw_json
		- Returns the raw json response provided by the API request
	

## Executing from a file
```py
from pyston import PystonClient
import asyncio

async def main():
	with open("test.py") as f:
		client = PystonClient()
		output = await client.execute("python",f)
		print(output)
		#Test code

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```