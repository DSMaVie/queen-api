import strawberry


@strawberry.type
class Event:
    name: str
    description: str
    id: int
