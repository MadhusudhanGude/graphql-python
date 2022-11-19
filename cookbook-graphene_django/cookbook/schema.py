import graphene

import apps.ingredients.schema
import apps.ingredients.relay_schema


class Query(
        apps.ingredients.schema.Query,
        # apps.ingredients.relay_schema.Query,
        graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(
    apps.ingredients.schema.Mutation,
        graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
