import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Questions, Answers, ByUser
# import .mutations as mt
# from faq.mutations import QuestionMutation, AddUser, UpdateLikes

class UserType(DjangoObjectType):
    class Meta:
        model=ByUser
        fields = ("username", "rating")

class QuestionType(DjangoObjectType):
    class Meta:
        model = Questions
        fields = ("title", "date_created")

        

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answers
        fields = ("questions", "answer_text", "likes", "dislikes", "byUser")


class Query(graphene.ObjectType):


    all_questions = graphene.Field(QuestionType, title=graphene.String())
    all_answers = graphene.List(AnswerType, title=graphene.String())
    total_question = graphene.List(QuestionType)

    def resolve_total_question(self,root, info):
        return Questions.objects.all()

    def resolve_all_questions(self,root, info, title):
        a = Questions.objects.get(title=title)
        return a

    def resolve_all_answers(self,root, info,title):
        # return Answers.objects.filter(questions) 
        a = Questions.objects.get(title=title).id
        return Answers.objects.filter(questions__title=title)

        


    # all_questions = DjangoListField(QuestionType)

    # all_questions = graphene.Field(QuestionType, title=graphene.String())
    # all_questions = graphene.List(QuestionType)
    # all_user = graphene.List(UserType)
    # all_answers = graphene.List(AnswerType)

    # all_answers = graphene.List(AnswerType, questions=graphene.String())



    # def resolve_all_questions(root, info):       
        # return Questions.objects.filter(title= title).first()
        # return Questions.objects.all()

    # def resolve_all_user(root, info):
    #     return ByUser.objects.all()   

    # def resolve_all_answers(root,info,title):
        # return Answers.objects.all()
        # return Answers.objects.filter(questions=questions)

class QuestionMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        newTitle = graphene.String(required=True)
        # newChange = graphene.String(required=True)

    questions = graphene.Field(QuestionType)
    # newTitle = graphene.Field(QuestionType)


    @classmethod
    def mutate(cls, root, info, title, newTitle):
        # c = Questions.objects.get(title=title)
        # c.title = newChange
        # c.save()

        # questions = Questions.objects.filter(title=title).update(title=newTitle)
        # newTitle = question.title
        # c = Questions(title=title)
        # questions.title = newTitle
        # questions.save()
        questions = Questions.objects.get(title=title)
        questions.title = newTitle

        questions.save()

        return QuestionMutation(questions)

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

class UpdateLikes(graphene.Mutation):
    class Arguments:
        ans = graphene.String(required=True)

    likes = graphene.Int()
    ansObject = graphene.Field(AnswerType)

    @classmethod
    def mutate(cls, root, info, ans):
        ansObject = Answers.getanswer.get_ans_object(ans)
        likes = Answers.getanswer.totallikes(ans)
        ansObject.likes = likes+1
        ansObject.save()
        return UpdateLikes(ansObject=ansObject)

class UpdatedisLikes(graphene.Mutation):
    class Arguments:
        ans = graphene.String(required=True)

    dislikes = graphene.Int()
    dislikeObject = graphene.Field(AnswerType)

    @classmethod
    def mutate(cls, root, info, ans):
        dislikeObject = Answers.getanswer.get_ans_object(ans)
        dislikes = Answers.getanswer.totaldislikes(ans)
        dislikeObject.dislikes = dislikes-1
        dislikeObject.save()
        return UpdatedisLikes(dislikeObject=dislikeObject)    

class deleteans(graphene.Mutation):
    class Arguments:
        ans = graphene.String(required=True)
        user = graphene.String(required= True)

    answer = graphene.Field(AnswerType)

    @classmethod
    def mutate(cls, root, info, ans,user):
        answer = Answers.getanswer.find_ans_by_user(ans,user) 
        answer.delete()
        return
        

class Mutation(graphene.ObjectType):

    update_questions = QuestionMutation.Field() #Working as Expected
    add_username = AddUser.Field()  ##Working as Expected
    update_likes_on_answer = UpdateLikes.Field()  ##Working as Expected
    update_dislikes_on_answer = UpdatedisLikes.Field() ##Working as Expected
    delete_ans = deleteans.Field() ##Working as Expected  

schema = graphene.Schema(query = Query, mutation= Mutation)



