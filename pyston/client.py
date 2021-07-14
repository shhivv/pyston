from .exceptions import InvalidLanguage
from typing import Optional,Union
from io import TextIOWrapper
from . import http_handler
import json
from .response import Output

class PystonClient:
    """Pyston client class"""
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = "https://emkc.org/api/v2/piston/",
    ):

        self.base_url = base_url
        self._http_session = http_handler.HTTP(self.base_url,api_key)    
    
    async def close_session(self):
        await self._http_session.close()

    async def get_runtimes(self, formatted: Optional[bool] = True):
        """ Returns the runtimes supported by the Piston API"""
        runtimes = await self._http_session.get_response("get", "runtimes/")
        if formatted:
            return json.dumps(runtimes, indent=4)
        else:
            return runtimes

    async def execute(
        self,
        language: str,
        code: Union[str, TextIOWrapper],
        version: Optional[str] = None,
        file_name: Optional[str] = "",
        stdin: Optional[str] = "",
        args: Optional[list] = [],
        compile_timeout: Optional[int] = 10000,
        run_timeout: Optional[int] = 3000,
        compile_memory_limit: Optional[int] = -1,
            run_memory_limit: Optional[int] = -1):
        """Executes the code"""

        payload = {
            "language": language,
            "stdin": stdin,
            "args": args,
            "compile_timeout": compile_timeout,
            "run_timeout": run_timeout,
            "compile_memory_limit": compile_memory_limit,
            "run_memory_limit": run_memory_limit
        }
        if version is None:
            payload["version"] = await self.get_latest_version(language)
        else:
            payload["version"] = version

        if isinstance(code,TextIOWrapper):
            payload["files"] = [{"name": file_name, "content": code.read()}]
        else:
            payload["files"] = [{"name": file_name, "content": code}]

        output = await self._http_session.get_response("post", 
                                                       "execute/", 
                                                       data=json.dumps(payload))
        return Output(output)

    async def _parse_runtimes(self):
        json_data = await self._http_session.get_response("get", "runtimes/")
        parsed_json = {}
        for element in json_data:
            parsed_json[element["language"]] = element            
        return parsed_json

    async def _parse_aliases(self):
        json_data = await self._http_session.get_response("get", "runtimes/")
        parsed_aliases = {}
        for langauge in json_data:
            version = langauge["version"]
            parsed_aliases[langauge["language"]] = version
            for alias in langauge["aliases"]:
                parsed_aliases[alias] = version
        return parsed_aliases

    async def get_aliases(self, language: str):
        try:
            parsed_runtimes = await self._parse_runtimes()
            return parsed_runtimes[language]["aliases"]
        except KeyError:
            raise InvalidLanguage(f"{language} not found")

    async def get_latest_version(self, language: str):
        try:
            parsed_aliases = await self._parse_aliases()
            return parsed_aliases[language]
        except KeyError:
            raise InvalidLanguage(f"{language} not found")

    async def get_language_info(self, language: str):
        try:
            parsed_runtimes = await self._parse_runtimes()
            return parsed_runtimes[language]
        except KeyError:
            raise InvalidLanguage(f"{language} not found")

    @property
    async def languages(self):
        runtimes = await self._http_session.get_response("get", "runtimes/")
        return [x["language"] for x in runtimes]

    @property
    def endpoints(self):
        return ("runtimes", "execute")
    