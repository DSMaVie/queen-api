from queen_api.gql.types import Event
import strawberry
from strawberry.types import Info


def test_coro(sesh):
    print("this is fresh")
    return None

@strawberry.type
class Query:
    @strawberry.field
    def events(self) -> list[Event]:
        return [Event(name="Quafe", description="An event to relax to", id=1)]

    @strawberry.field
    async def test(self, info: Info) -> str:
        handler = info.context["query_handler"]
        await handler.handle(test_coro)
        return "good"
