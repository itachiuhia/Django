import graphene
from graphene_django.types import DjangoObjectType
from .forms import UserRegistrationForm

from authorization.models import User_Profile

class User_ProfileType(DjangoObjectType):
    class Meta:
        model = User_Profile
        fields = ("username", "email", "rating", "questions", "answers")


class Query(graphene.ObjectType):
    profile = graphene.Field(User_Profile)

class RegisterProfile(graphene.Mutation):
    form_class = UserRegistrationForm
    

class Mutation(graphene.ObjectType):
    register_profile = RegisterProfile.Field()
    


schema = graphene.Schema(query=Query, mutation = Mutation)