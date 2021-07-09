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


<br>


- **execute()**
	- Used to execute code through the Piston API
	- Parameters
		- `language : str`
		- `code : str`
		- `version : Optional[str]`
		- `file_name: Optional[str]`
		- `stdin: Optional[str]`
		- `args: Optional[list]`
		- `compile_timeout: Optional[int]`
		- `run_timeout: Optional[int]`
		- `compile_memory_limit: Optional[int]`
		- `run_memory_limit: Optional[int]`

	- Returns a Output object

- **get_aliases()**
	- Used to fetch the aliases of the languages supported by the Piston API
	- Parameters
		- `language : str`

	- Returns a dict

- **get_latest_version()**
	- Used to fetch the latest version of a language supported by the Piston API
	- Parameters
		- `language : str`
		
	- Returns a int

- **get_language_info()**
	- Used to fetch the latest version and the aliases of a languages supported by the Piston API
	- Parameters
		- `language : str`
		
	- Returns a dict

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