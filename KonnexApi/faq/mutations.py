from faq.schema import  UserType,QuestionType, AnswerType
from .models import Questions, Answers, ByUser
import graphene


class QuestionMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        # newChange = graphene.String(required=True)

    questions = graphene.Field(QuestionType)

    @classmethod
    def mutate(cls, root, info, title):
        c = Questions.objects.get(title=title)
        # c.title = newChange
        # c.save()

        c = Questions(title=title)
        c.save()

        return QuestionMutation(title=title)

class AddUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        rating = graphene.Int(required=True)

    byuser = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, username, rating):
        byUser = ByUser(username=username, rating = rating)
        byUser.save()
        return AddUser(byUser)
        # return AddUser(username=username, rating=rating)

        # return ByUser(username=username, rating = rating)

class UpdateLikes(graphene.Mutation):
    class Arguments:
        ans = graphene.String(required=True)

    likes = graphene.Field(AnswerType)

    @classmethod
    def mutate(cls, root, info, ans):
        likes = Answers.getanswer.totallikes(ans)
        likes - likes+1
        likes.save()
        return UpdateLikes(likes)