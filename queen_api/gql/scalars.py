from typing import NewType
import strawberry
from queen_api.models import utils

AdChannels = strawberry.scalar(
    NewType("AdChannels", utils.AdChannels),
    description="an integer representation of the bitwise AdChannel Flags",
    serialize=lambda v: v.value,
    parse_value=lambda v: utils.AdChannels(v),
)
