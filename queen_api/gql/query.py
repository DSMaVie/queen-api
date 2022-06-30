import logging

import strawberry
from queen_api.db.queries import test_query

# from queen_api.gql.types import Event

logger = logging.getLogger(__name__)


@strawberry.type
class Query:
    # @strawberry.field
    # def events(self) -> list[Event]:
    #     return [Event(name="Quafe", description="An event to relax to", id=1)]

    @strawberry.field
    async def test(self) -> str:
        return await test_query()  # type: ignore
