import graphene
from graphene_django import DjangoObjectType
from .models import Item
from django.contrib.auth import get_user_model

User = get_user_model()

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ['username']

class ItemType(DjangoObjectType):
    class Meta:
        model = Item
        fields = ('id', 'title', 'status', 'image_url')

class ItemUser(graphene.Union):
    class Meta:
        types = (ItemType, UserType)

# TODO: Advance - search item by user id
class Query(graphene.ObjectType):
    all_items = graphene.List(ItemUser)
    get_item = graphene.Field(ItemUser,  id=graphene.Int())

    def resolve_all_items(root, info):
        return Item.objects.all()
    def resolve_get_item(root, info, id):
        return Item.objects.get(pk=id)


class AddItemMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)

    item = graphene.Field(ItemType)
    
    @classmethod
    def mutate(cls,root, info, title):
        item = Item(title=title)
        item.save()
        return AddItemMutation(item=item)

class UpdateItemMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String(required=True)

    item = graphene.Field(ItemType)
    
    @classmethod
    def mutate(cls,root, info, title, id):
        item = Item.objects.get(id=id)
        item.title = title
        item.save()
        return UpdateItemMutation(item=item)


class DeleteItemMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    item = graphene.Field(ItemType)
    
    @classmethod
    def mutate(cls,root, info, id):
        item = Item.objects.get(id=id)
        item.delete()
        return 

class Mutation(graphene.ObjectType):
    add_item = AddItemMutation.Field()
    update_item = UpdateItemMutation.Field()
    delete_item = DeleteItemMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

# Test query
# {
#     allItems{
#         ... on ItemType {
#             id
#             title
#             imageUrl
#             status
#         }
#         ... on UserType {
#             username
#         }
#     }
# }
