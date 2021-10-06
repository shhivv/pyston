.. pyston documentation master file, created by
   sphinx-quickstart on Sun Oct  3 16:14:26 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Pyston
==================================
An asynchronous API wrapper for the Piston API.

.. note:: The documentation of Piston API can be found at https://piston.readthedocs.io/en/latest/api-v2/

Features
---------
- Modern Pythonic API using ``async`` and ``await`` .
- 100% API coverage
- Easy to use 

Installation
-------------
**Downloading from PyPi (Recommended)**

.. tab-set::
   
   .. tab-item:: Linux or MacOS

      .. code-block:: sh
         
         $ python3 -m pip install aiopyston
      
   .. tab-item:: Windows
      
      .. code-block:: sh
         
         $ py -3 -m pip install aiopyston


**Downloading from source**

.. tab-set::
   
   .. tab-item:: Linux or MacOS

      .. code-block:: sh
         
         $ python3 -m pip install git+https://github.com/ffaanngg/pyston.git
      
   .. tab-item:: Windows

      .. code-block:: sh
         
         $ py -3 -m pip install git+https://github.com/ffaanngg/pyston.git


**Basic example**

.. code-block:: python

   from pyston import PystonClient,File
   import asyncio

   async def main():
      client = PystonClient()
      output = await client.execute("python",
      [
         File("print('Hello world')")
      ])
      print(output)

   loop = asyncio.get_event_loop()
   loop.run_until_complete(main())

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   reference
   Examples
   