from typing import Any, Literal
from motor.motor_asyncio import AsyncIOMotorClientSession

CollectionType = Literal["event"]


async def add(
    sesh: AsyncIOMotorClientSession,
    collection: CollectionType,
    data: Any,  # TODO: proper typing
):
    coll = sesh.client.get_default_database()[collection]

    insert_answer = await coll.insert_one(data.to_dict())
    return insert_answer.inserted_id

# TODO: define what to insert
# some data modeling ... from request to end