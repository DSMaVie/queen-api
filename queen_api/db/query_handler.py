from typing import Any, Awaitable, Callable, Concatenate, ParamSpec
from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorClientSession,
    AsyncIOMotorDatabase,
)
from queen_api.config import Config
import asyncio

queryParams = ParamSpec("queryParams")


class QueryHandler:
    def __init__(self, conf: Config) -> None:
        self.__uri = (
            f"mongodb://{conf.DB_USER}:{conf.DB_PASS}"
            + f"@{conf.DB_HOST}:{conf.DB_PORT}/{conf.DB_DEFAULT_DATABASE}"
        )
        self.__client = AsyncIOMotorClient(self.__uri)
        self.__client.get_io_loop = asyncio.get_running_loop

    async def handle(
        self,
        query: Callable[
            Concatenate[AsyncIOMotorClientSession, queryParams],
            Awaitable[Any],
        ],
        *args: queryParams.args,
        **kwargs: queryParams.kwargs,
    ):
        print(f"starting sesh in loop {asyncio.get_running_loop()}")
        async with await self.__client.start_session() as sesh:
            print(f"received {query=}")
            return sesh.with_transaction(lambda s: query(s, *args, **kwargs))

    # TODO: validate query
    # TODO: logging!!!!!
