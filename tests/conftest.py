import pytest
from queen_api.config import Config
from queen_api.main import get_server


@pytest.fixture(scope="module")
def conf():
    return Config(
        DB_HOST="www.example.com",
        DB_PORT=42069,
        DB_USER="magdalena",
        DB_PASS="some_safe_pw",
        DB_DEFAULT_DATABASE="test",
        SERVER_HOST="queen.api.com",
        SERVER_PORT=69420,
        DEBUG=True,
    )


@pytest.fixture(scope="module")
def server(conf):
    return get_server(conf)


@pytest.fixture(scope="module")
def schema(server):
    return server.schema

