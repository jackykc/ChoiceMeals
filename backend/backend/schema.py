import graphene
import simple_app.schema

class Queries(
	simple_app.schema.Query,
    graphene.ObjectType
):
    pass

class Mutations(
    simple_app.schema.Mutation,
    graphene.ObjectType,
):
    pass
    
schema = graphene.Schema(query=Queries, mutation=Mutations)