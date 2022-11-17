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

schema = graphene.Schema(query=Query)

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
