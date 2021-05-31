from django.urls import path
from graphene_django.views import GraphQLView
from faq.schema import schema

urlpatterns = [
    # only a single url to work with
    path("graphql", GraphQLView.as_view(graphiql = True, schema = schema)),

]