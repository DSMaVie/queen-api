from strawberry.asgi import GraphQL
from typing import Any

from starlette.requests import Request
from starlette.websockets import WebSocket
from starlette.responses import Response

from queen_api.config import Config


class QueenApiServer(GraphQL):
    def __init__(self, conf: Config, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.conf = conf

    async def get_context(
        self, request: Request | WebSocket, response: Response = None
    ) -> Any:
        return {"conf": self.conf, "request": request, "response": response}
