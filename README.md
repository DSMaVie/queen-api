
# Queer Event Editor and Navigator (QuEEN)

This is now the third time I retry this project. First I tired this the classic way with Flask and
an sqlite database which I queried with plaintext SQL.

The second iteration was started because I experimented with poetry. This one included a FastAPI and
at least SQLAlchemy as an ORM. Additionally, I experimented with Pydantic to enforce the schema.

You know, what they say: Third times a charm! So here it is:

QuEEN, the Queer Event Editor and Navigator, a GraphQL API for a MongoDB. Hopefully this time we will
not abbandon the project due to unforeseeable circumstances (studies).


## Setup

Since this project relies on [poetry](https://python-poetry.org/), you need this installed. The `python`
version used is `3.10.2`. You need to have that installed before installing all dependencies with:

```bash
poetry install
```

The GraphQL API itself uses [strawberry](https://strawberry.rocks) and for now its developement server.
You can start it with:

```bash
poetry run strawberry server queen_api.main:schema
```