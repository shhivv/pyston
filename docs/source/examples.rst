Examples
========

**Fetching all the runtimes supported**

.. code-block:: python

    from pyston import PystonClient,File
    import asyncio

    async def main():
        client = PystonClient()
        runtimes = await client.runtimes()
        print(runtimes)

    asyncio.get_event_loop().run_until_complete(main())

**Multiple file example**

.. code-block:: python

    from pyston import PystonClient,File
    import asyncio


    file2_content = """

    def square(num):
        return num*num

    """

    file1_content = """
    import file2

    print(file2.square(4))
    """

    file1 = File(file1_content,filename="file1.py")
    file2 = File(file2_content,filename="file2.py")

    async def main():
        client = PystonClient()
        output = await client.execute(
            "python",
            [file1,file2]
        )

        print(output)

    asyncio.get_event_loop().run_until_complete(main())

**Executing from a file**

.. code-block:: python

    from pyston import PystonClient,File
    import asyncio

    async def main():

        with open('test.py') as f:
            file = File(f)
            
        client = PystonClient()
        output = await client.execute(
            "python",
            [file]
        )

        print(output)

    asyncio.get_event_loop().run_until_complete(main())