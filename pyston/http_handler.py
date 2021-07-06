import aiohttp
import sys
import asyncio
from . import __version__
from .exceptions import *
from typing import Optional

class HTTP:
    def __init__(self, apikey: str):
        self.BASE_URL = "https://emkc.org/api/v2/piston/"        
        self._headers = {}
        if apikey is not None:
            self._headers["Authorization"] = apikey
        self._headers["User-Agent"] = f"Pyston https://github.com/ffaanngg/pyston {__version__} {sys.version_info} {aiohttp.__version__}"
        self._headers['Content-Type'] = 'application/json'
        self._setup()



    def _setup(self):
        self._loop = asyncio.get_event_loop()
        self._session = aiohttp.ClientSession(headers=self._headers,loop=self._loop)

        
    async def _request(self, method: str, endpoint: str, data: str):
        if data is None:
            async with self._session.request(method,self.BASE_URL + endpoint) as response:
                return response, await response.json()
        else:
            async with self._session.request(method,self.BASE_URL + endpoint, 
                                        data=data) as response:
                return response, await response.json()

    async def get_response(self, method: str, endpoint: str, data: Optional[str] = None):

        response, response_json = await self._request(method, endpoint, data)

        if 300 > response.status >= 200:
            return response_json
        elif response.status == 429:
            raise TooManyRequests("You have been ratelimited.Try again later")
        elif response.status == 500:
            raise InternalServerError("Server failed to respond. Try again later")
        elif response.status == 404:
            raise RuntimeNotFound("Invalid language or version")
        elif response.status == 400:
            raise InvalidArgumentType(response_json["message"])
        else:
            raise UnexpectedError(await response.text())

    async def close(self):
        await self._session.close()

    def __del__(self):
        self._loop.create_task(self.close())
