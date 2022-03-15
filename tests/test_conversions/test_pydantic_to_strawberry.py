from datetime import datetime
import pytest

from queen_api.models import event
from queen_api.models.utils import AdChannels


@pytest.fixture
def an_event():
    return event.Event(
        id="some_id",
        name="some_name",
        description="some event",
        ad_channels=AdChannels.calender | AdChannels.instagram,
        start=datetime.today(),
        created_at=datetime.now(),
        last_changed=datetime.now(),
    )


def test_pydatic_to_dict(an_event):
    an_event.dict(exclude_unset=True, exclude_none=True)


def test_dict_to_pydantic(an_event):
    a_dict = an_event.dict(exclude_unset=True, exclude_none=True)
    event_from_dict = event.Event(**a_dict)
    assert event_from_dict.ad_channels == an_event.ad_channels
