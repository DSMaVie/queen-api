from typing import Literal

from motor.motor_asyncio import AsyncIOMotorClientSession
from queen_api.db.controller import HANDLE_QUERY
from queen_api.models.event import InputEvent

CollectionType = Literal["event"]


@HANDLE_QUERY
async def add(
    sesh: AsyncIOMotorClientSession,
    collection: CollectionType,
    data: InputEvent,
):
    coll = sesh.client.get_default_database()[collection]

    insert_answer = await coll.insert_one(data.dict())
    return insert_answer.inserted_id
