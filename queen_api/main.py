import logging

import strawberry
import uvicorn
from strawberry.asgi import GraphQL

from queen_api import gql
from queen_api.config import get_config

logger = logging.getLogger(__name__)


def get_server() -> GraphQL:
    logger.info("initializing server...")
    schema = strawberry.Schema(query=gql.Query)  # , mutation=gql.Mutation)
    logger.info("finished initializing server.")
    return GraphQL(schema)


if __name__ == "__main__":
    conf = get_config()
    server = get_server()

    logger.info("starting uvicorn loop...")
    uvicorn.run(
        server,  # type: ignore
        host=conf.SERVER_HOST,
        port=conf.SERVER_PORT,
        log_level="debug" if conf.DEBUG else "warning",
    )
