from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from queen_api.models.utils import AdChannels


class DbEntry(BaseModel):
    """a model every database entry can subclass from. just supplies an id."""

    id: str


class EventInfo(BaseModel):
    """for subclassing. contains the general info of an event, either in template
    or timed form."""

    name: str
    description: Optional[str] = None
    assignee: Optional[str] = None
    ad_channels: AdChannels = AdChannels(0)

    created_at: datetime
    last_changed: datetime

    class Config:
        use_enum_values = True

    # @validator("ad_channels")
    # def parse_ad_channels(cls, ad_channels):
    #     match ad_channels:
    #         case str():
    #             if ad_channels not in (channel.name for channel in AdChannels):
    #                 raise ValueError(
    #                     f"{ad_channels=} must be an appropriate ad_channel!"
    #                 )
    #             return AdChannels[ad_channels]

    #         case int():
    #             if ad_channels not in AdChannels:
    #                 raise ValueError(
    #                     f"{ad_channels=} must be an appropriate ad_channel!"
    #                 )
    #             return AdChannels(ad_channels)

    #         case AdChannels():
    #             return ad_channels

    #         case _:
    #             raise ValueError(f"unknown value for {ad_channels=}")

    #     # TODO: catch case of composed Ad Channels?


class EventTimed(BaseModel):
    """this model describes an event that has a start and end time. this does not exist
    for template events (later)."""

    start: datetime
    end: Optional[datetime] = None


class Event(DbEntry, EventInfo, EventTimed):
    """This model describes an entire event, that has been saved in the database."""

    pass


class InputEvent(EventInfo, EventTimed):
    """This class shows how the data comming from the frontend looks like."""

    pass
