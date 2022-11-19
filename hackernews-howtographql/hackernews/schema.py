import graphene
import graphql_jwt
import apps.links.schema
import apps.links.schema_relay
import apps.users.schema


class Query(
        apps.links.schema.Query,
        apps.users.schema.Query,
        apps.links.schema_relay.RelayQuery,
        graphene.ObjectType):
    pass


class Mutation(
        apps.links.schema.Mutation,
        apps.users.schema.Mutation,
        apps.links.schema_relay.RelayMutation,
        graphene.ObjectType):

    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
