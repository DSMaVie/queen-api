from queen_api.gql.types import Event
import strawberry


@strawberry.type
class Query:
    @strawberry.field
    def events(self) -> list[Event]:
        return [Event(name="Quafe", description="An event to relax to", id=1)]
