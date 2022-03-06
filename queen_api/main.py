import strawberry
import uvicorn
from queen_api import gql
from dotenv import dotenv_values, find_dotenv
from queen_api.config import Config
from queen_api.server import QueenApiServer


def get_config():
    dotenv_path = find_dotenv(".env")
    return Config(**dotenv_values(dotenv_path))  # type: ignore


def get_server(conf: Config):
    schema = strawberry.Schema(query=gql.Query, mutation=gql.Mutation)
    return QueenApiServer(conf, schema)


if __name__ == "__main__":
    conf = get_config()
    server = get_server(conf)

    uvicorn.run(
        server,  # type: ignore
        host=conf.SERVER_HOST,
        port=conf.SERVER_PORT,
        log_level="debug" if conf.DEBUG else "info",
    )
