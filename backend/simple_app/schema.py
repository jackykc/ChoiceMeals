import graphene
from graphene_django.types import DjangoObjectType
from graphql_relay.node.node import from_global_id
from django.contrib.auth.models import User
import json

from .models import Category, Ingredient

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient

class UserType(DjangoObjectType):
    class Meta:
        model = User

class Query(graphene.AbstractType):
    category = graphene.Field(CategoryType,
                              id=graphene.ID(),
                              name=graphene.String()
                              )

    ingredient = graphene.Field(IngredientType,
                              id=graphene.ID(),
                              name=graphene.String()
                              )
    
    all_categories = graphene.List(CategoryType)
    all_ingredients = graphene.List(IngredientType)
    current_user = graphene.Field(UserType)
    
    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Category.objects.get(pk=id)

        if name is not None:
            return Category.objects.get(name=name)

        return None

    def resolve_ingredient(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Ingredient.objects.get(pk=id)

        if name is not None:
            return Ingredient.objects.get(name=name)

        return None

    def resolve_current_user(self, info, **kwargs):
        if not info.context.user.is_authenticated:
            return None
        return info.context.user

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        return Ingredient.objects.select_related('category').all()



# class MessageType(DjangoObjectType):
#     class Meta:
#         model = models.Message
#         interfaces = (graphene.Node, )



# class CreateMessageMutation(graphene.Mutation):
#     class Arguments:
#         message = graphene.String()

#     status = graphene.Int()
#     formErrors = graphene.String()
#     message = graphene.Field(MessageType)

#     @staticmethod
#     def mutate(self, info, **args):
#         if not info.context.user.is_authenticated:
#             return CreateMessageMutation(status=403)
#         message = args.get('message', '').strip()
#         # Here we would usually use Django forms to validate the input
#         if not message:
#             return CreateMessageMutation(
#                 status=400,
#                 formErrors=json.dumps(
#                     {'message': ['Please enter a message.']}))
#         obj = models.Message.objects.create(
#             user=info.context.user, message=message
#         )
#         return CreateMessageMutation(status=200, message=obj)


# class Mutation(graphene.AbstractType):
#     create_message = CreateMessageMutation.Field()

# class Query(graphene.AbstractType):
#     message = graphene.Field(MessageType, id=graphene.ID())

#     def resolve_message(self, info, **args):
#         rid = from_global_id(args.get('id'))
#         # rid is a tuple: ('MessageType', '1')
#         return models.Message.objects.get(pk=rid[1])


#     all_messages = graphene.List(MessageType)

#     def resolve_all_messages(self, info, **args):
#         return models.Message.objects.all()
