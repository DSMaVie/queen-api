from queen_api.graphql.types import Event
from typing import List
import strawberry


@strawberry.type
class Query:
    @strawberry.field
    def events(self) -> List[Event]:
        return [Event(name="Quafe", description="An event to relax to", id=1)]
