import pytest

from queen_api.db.query_handler import QueryHandler
from queen_api.config import Config
from starlette.requests import Request


@pytest.mark.asyncio
async def test_server_get_context(server):
    server_ctx = await server.get_context(
        request=Request({"type": "http"}), response=None
    )

    assert isinstance(
        server_ctx["conf"], Config
    ), "server context should contain the ctx."
    assert isinstance(
        server_ctx["query_handler"], QueryHandler
    ), "server context should contain the ctx."
