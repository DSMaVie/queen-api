# import strawberry

# from queen_api.gql.types import Event


# @strawberry.type
# class Mutation:
#     @strawberry.mutation
#     def add_event(self, name: str, id: int, description: str) -> Event:
#         event = Event(name=name, description=description, id=id)
#         print(f"{event=}")
#         return event
