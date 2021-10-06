Reference
==============

A ``PystonClient`` instance must be made to access the Piston API.

*class* PystonClient
----------------------

Parametres
    - ``api_key`` (Optional[str]) = ``None``
        The API key used when requesting the Piston API.

    - ``base_url`` (Optional[str]) = ``"https://emkc.org/api/v2/piston/"``
        The parametre can be used for self-hosted piston instances.


Methods
    *async* ``runtimes`` ()
        Returns the runtimes supported by the Piston API.

        **Return type** - List[ :ref:`Runtime<Runtime>` ]


    *async* ``execute`` (
        ``language``,

        ``files``,

        ``version``,

        ``stdin``,
        
        ``args``,

        ``compile_timeout``,

        ``run_timeout``,

        ``compile_memory_limit``,

        ``run_memory_limit``)

        Executes the files in the Piston API.

        **Parameters**

        - ``language`` ( ``str`` )
            The language of the files to execute.

        - ``files`` (List[ :ref:`File<File>` ])
            The files to execute.

        - ``version`` ( ``Optional[str]`` ) = "*"
            The version of the language to execute.

        - ``stdin`` ( ``Optional[str]`` ) = ""
            The stdin to use when executing the files.

        - ``args`` ( ``Optional[list]`` ) = []
            The arguments to pass to the files.

        - ``compile_timeout`` ( ``Optional[int]`` ) = 10000
            The timeou for the compilation stage.

        - ``run_timeout`` ( ``Optional[int]`` ) = 3000
            The timeout for the execution stage.

        - ``compile_memory_limit`` ( ``Optional[int]`` ) = -1
            The memory limit for the compilation stage.

        - ``run_memory_limit`` ( ``Optional[int]`` ) = -1
            The memory limit for the execution stage.


        **Return type** - :ref:`Output<Output>`

    *async* ``get_runtimes`` ( ``language``)
        Returns the supported runtimes for a language.
        
        ie: ``deno`` and ``nodejs`` for javascript.

        **Return type** - List[ :ref:`Runtime<Runtime>` ]

    *async* ``languages`` ()
        Returns the languages supported by the Piston API.

        **Return type** - ``Set[str]``


.. _File:

*class* File
-------------

Parametres
    - ``content`` ( ``str`` )
        Content of the file to be executed
    
    - ``filename`` ( ``str`` ) = ``None``
        Filename will be randomized if not provided.


.. _Output:

*class* Output
----------------------

Attributes
    - ``language`` ( ``str`` ) - Language of code executed.

    - ``version`` ( ``str`` ) - Version of runtime used.

    - ``raw_json`` ( ``dict`` ) - The recieved JSON response from the executing API call.

    - ``run_stage`` (  :ref:`RunStage<RunStage>`  ) - The run stage of the execution.

    - ``compile_stage`` (  :ref:`CompileStage<CompileStage>`  ) - The compile stage of the execution. Defaults to ``None`` if compile stage does not exist.


Methods
    *property* success
        Returns whether the program executed properly

        **Return Type** - ``bool``

.. _RunStage:

*class* RunStage
-----------------

Attributes
    -   ``stdout`` ( ``str`` ) - Stdout from program execution.

    -   ``stdrr`` ( ``str`` ) - Stdrr from program execution.

    -   ``output`` ( ``str`` ) - Output from program execution.

    -   ``code`` ( ``Any`` ) - Exit code from program execution.

    -   ``signal`` ( ``Any`` ) - signal from program execution.    

.. _CompileStage:

*class* CompileStage
-----------------

Attributes
    -   ``stdout`` ( ``str`` ) - Stdout from program compilation
    
    -   ``stdrr`` ( ``str`` ) - Stdrr from program compilation.

    -   ``output`` ( ``str`` ) - Output from program compilation.

    -   ``code`` ( ``Any`` ) - Exit code from program compilation.

    -   ``signal`` ( ``Any`` ) - signal from program compilation.    

.. _Runtime:

*class* Runtime
-----------------

Attributes
    - ``language`` ( ``str`` ) - Language of runtime.

    - ``version`` ( ``str`` ) - Version of runtime.
    
    - ``runtime`` ( ``Any`` ) - Runtime name of that runtime or None if it doesn't exist.