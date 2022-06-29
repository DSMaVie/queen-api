import asyncio
import functools
import logging
from typing import Any, Awaitable, Callable, Concatenate, ParamSpec

from dotenv import dotenv_values, find_dotenv
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorClientSession
from queen_api.config import Config

logger = logging.getLogger(__name__)

queryParams = ParamSpec("queryParams")


class HandleQuery:
    def __init__(self, conf: Config) -> None:
        self.__uri = (
            f"mongodb://{conf.DB_USER}:{conf.DB_PASS}"
            + f"@{conf.DB_HOST}:{conf.DB_PORT}/{conf.DB_DEFAULT_DATABASE}"
        )
        logger.info(f"connecting to {self.__uri}...")
        self.__client = AsyncIOMotorClient(self.__uri)
        self.__client.get_io_loop = asyncio.get_running_loop
        logger.info("finished initializing database connection.")

    async def __call__(
        self,
        query: Callable[
            Concatenate[AsyncIOMotorClientSession, queryParams],
            Awaitable[Any],
        ],
    ):
        @functools.wraps(query)
        async def wrapper(*args: queryParams.args, **kwargs: queryParams.kwargs):
            async with await self.__client.start_session() as sesh:
                logger.debug(f"starting sesh in loop {asyncio.get_running_loop()}.")
                logger.debug(f"running {query=}")
                return await query(sesh, *args, **kwargs)

        return wrapper


def get_query_handler_from_conf(
    dict_conf: dict[str, str | None] | None = None
) -> HandleQuery:
    if not dict_conf:
        dict_conf = dotenv_values(find_dotenv())
    conf = Config(**dict_conf)  # type: ignore
    # types are ignored here so that missing args are failing immediately
    return HandleQuery(conf=conf)


HANDLE_QUERY = get_query_handler_from_conf()
