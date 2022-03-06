from strawberry.asgi import GraphQL
from strawberry.dataloader import DataLoader
from typing import Any, Optional

from starlette.requests import Request
from starlette.websockets import WebSocket
from starlette.responses import Response

from queen_api.config import Config
from queen_api.db.query_handler import QueryHandler


class QueenApiServer(GraphQL):
    def __init__(self, conf: Config, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.conf = conf
        self.query_handler = QueryHandler(conf)

    async def get_context(
        self, request: Request | WebSocket, response: Optional[Response]
    ) -> Any:

        return {
            "conf": self.conf,
            "query_handler": self.query_handler,
            "request": request,
            "response": response,
        }
