from django.urls import path
from . import views
from graphene_django.views import GraphQLView
from .schema import schema

urlpatterns = [
    path('', views.index),
    path('search/', views.item_search_views),
    path('create/', views.item_create_views),
    path('graphql', GraphQLView.as_view(graphiql=True, schema=schema))
]
