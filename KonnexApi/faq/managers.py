from django.db import models


class PostQuerySet(models.QuerySet):
    def get_answerby(self,user):
        return self.filter(byUser__username=user)

    def get_allquestions(self,quest):
        return self.filter(questions__title=quest)    

    def count_total_likes(self, ans):
        # print(self.get(answer_text=ans).likes)
        return self.get(answer_text=ans).likes 

    def count_total_dislikes(self, ans):
        return self.get(answer_text=ans).dislikes   

    def find_answers_by_user(self, ans, user):
        return self.filter(answer_text= ans, byUser__username=user)  

    def get_answers_object(self, ans):
        return self.get(answer_text=ans)        



class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self.db)

    def allquestions(self, quest):
        return self.get_queryset().get_allquestions(quest)

    def answerby(self,user):
        return self.get_queryset().get_answerby(user)

    def totallikes(self, ans):
        return self.get_queryset().count_total_likes(ans)  

    def totaldislikes(self, ans):
        return self.get_queryset().count_total_dislikes(ans)          

    def find_ans_by_user(self, ans, user):
        return self.get_queryset().find_answers_by_user(ans,user)

    def get_ans_object(self, ans):
        return self.get_queryset().get_answers_object(ans)    

