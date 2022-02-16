import strawberry
from queen_api import graphql


schema = strawberry.Schema(query=graphql.Query, mutation=graphql.Mutation)
