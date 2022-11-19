import graphene

from graphene_django.types import DjangoObjectType

from apps.ingredients.models import Category, Ingredient
from graphene_django.debug import DjangoDebug

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient


class Query(graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='_debug')
    
    category = graphene.Field(CategoryType,
                              id=graphene.Int(),
                              name=graphene.String())
    all_categories = graphene.List(CategoryType)


    ingredient = graphene.Field(IngredientType,
                                id=graphene.Int(),
                                name=graphene.String())
    all_ingredients = graphene.List(IngredientType)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        return Ingredient.objects.all()

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


class CategoryMutation(graphene.Mutation):
    # The class attributes define the response of the mutation
    category = graphene.Field(CategoryType)

    class Arguments:
        # The input arguments for this mutation
        name = graphene.String(required=True)
        id = graphene.ID()

    def mutate(self, info, name, id):
        category = Category.objects.get(pk=id)
        category.name = name
        category.save()
        # Notice we return an instance of this mutation
        return CategoryMutation(category=category)


class Mutation(graphene.ObjectType):
    update_category = CategoryMutation.Field()