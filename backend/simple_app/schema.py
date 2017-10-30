import graphene
from graphene_django.types import DjangoObjectType
from graphql_relay.node.node import from_global_id
from django.contrib.auth.models import User
import json

from .models import Category, Ingredient, Recipe

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient

class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe

class UserType(DjangoObjectType):
    class Meta:
        model = User

class Query(graphene.ObjectType):
    category = graphene.Field(CategoryType,
                              id=graphene.ID(),
                              name=graphene.String()
                              )

    ingredient = graphene.Field(IngredientType,
                              id=graphene.ID(),
                              name=graphene.String(),
                              notes=graphene.String(),
                              serving_size=graphene.Int(),
                              calories=graphene.Int(),
                              fat=graphene.Int(),
                              cholesterol=graphene.Int()
                              )
    
    # recipe = graphene.Field(RecipeType,
    #                         id=graphene.ID(),

    #                         )

    current_user = graphene.Field(UserType)
    
    all_categories = graphene.List(CategoryType)
    all_ingredients = graphene.List(IngredientType)
    all_recipes = graphene.List(RecipeType)

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

    def resolve_all_recipes(self, info, **kwargs):
        return Recipe.objects.all()

class CreateCategoryMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    status = graphene.Int()
    formErrors = graphene.String()
    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(self, info, **kwargs):
        name = kwargs.get('name')
        if not name:
            return CreateCategoryMutation(
                status=400,
                formErrors=json.dumps(
                    {'name': ['Please enter a category.']}
                )
            )

        obj = Category.objects.create(
            name=name
        )
        return CreateCategoryMutation(status=200, category=obj)

class CreateIngredientMutation(graphene.Mutation):
    class Arguments:
        category_name = graphene.String()
        serving_size = graphene.Int()

    status = graphene.Int()
    formErrors = graphene.String()
    ingredient = graphene.Field(IngredientType)

    @staticmethod
    def mutate(self, info, **kwargs):
        category_name = kwargs.get('category_name')
        serving_size = kwargs.get('serving_size')
        if (not category_name):
            return CreateIngredientMutation(
                status=400,
                formErrors=json.dumps(
                    {'category': ['Choose an existing category']}
                )
            )
        
        if not serving_size:
            return CreateIngredientMutation(
                status=400,
                formErrors=json.dumps(
                    {'serving_size': ['Please enter a serving size.']}
                )
            )

        category = Category.objects.get(name=category_name)
        if not category:
            return CreateIngredientMutation(
                status=400,
                formErrors=json.dumps(
                    {'category': ['Choose an existing category']}
                )
            )

        obj = Ingredient.objects.create(
            category=category,
            serving_size=serving_size
        )
        return CreateIngredientMutation(status=200, ingredient=obj)

class Mutation(graphene.ObjectType):
    create_category = CreateCategoryMutation.Field()
    create_ingredient = CreateIngredientMutation.Field()
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
