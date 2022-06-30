import strawberry
from queen_api.models import event


@strawberry.experimental.pydantic.type(
    model=event.InputEvent, description="An Event of the Queerreferat", all_fields=True
)
class Event:
    pass
