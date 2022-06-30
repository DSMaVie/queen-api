import asyncio
import logging

from motor.motor_asyncio import AsyncIOMotorClientSession
from queen_api.db.controller import HANDLE_QUERY

# from typing import Literal

# from queen_api.models.event import InputEvent

# CollectionType = Literal["event"]
logger = logging.getLogger(__name__)

# @HANDLE_QUERY
# async def add(
#     sesh: AsyncIOMotorClientSession,
#     collection: CollectionType,
#     data: InputEvent,
# ):
#     coll = sesh.client.get_default_database()[collection]

#     insert_answer = await coll.insert_one(data.dict())
#     return insert_answer.inserted_id


@HANDLE_QUERY
async def test_query(sesh: AsyncIOMotorClientSession):
    await asyncio.sleep(1)
    logger.debug(f"connected to db at {sesh.cluster_time}")
    return "test completed"
