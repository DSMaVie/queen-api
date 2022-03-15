from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validator

from queen_api.models.utils import AdChannels


class DbEntry(BaseModel):
    id: str


class EventInfo(BaseModel):
    name: str
    description: Optional[str] = None
    assignee: Optional[str] = None
    ad_channels: AdChannels = AdChannels(0)

    created_at: datetime
    last_changed: datetime

    class Config:
        use_enum_values = True

    @validator
    def parse_ad_channels(cls, ad_channels):
        match type(ad_channels):
            case str:
                if ad_channels not in (channel.name for channel in AdChannels):
                    raise ValueError(
                        f"{ad_channels=} must be an appropriate ad_channel!"
                    )
                return AdChannels[ad_channels]

            case int:
                if ad_channels not in AdChannels:
                    raise ValueError(
                        f"{ad_channels=} must be an appropriate ad_channel!"
                    )
                return AdChannels(ad_channels)

            case AdChannels:
                return ad_channels

            case _:
                raise ValueError(f"unknown value for {ad_channels=}")

        # why is this not working


class TimedEntry(BaseModel):
    start: datetime
    end: Optional[datetime] = None


class Event(DbEntry, EventInfo, TimedEntry):
    pass


class InputEvent(EventInfo, TimedEntry):
    pass
