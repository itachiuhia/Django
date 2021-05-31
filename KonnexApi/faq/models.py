from django.db import models
from django.conf import settings
from .managers import PostManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

# class Queries(models.Model):
#     quest = models.CharField(max_length=200)
#     ans = models.CharField(max_length=200)
#     byUser = models.CharField(max_length=20)
#     like = models.IntegerField(null=True)
#     dislike = models.IntegerField(null=True)

#     def __str__(self):
#         return self.quest

class ByUser(models.Model):
    username = models.CharField(max_length=100, verbose_name="username")
    # answers =models.ManyToManyField(Answers, related_name="answers")
    # questions = models.ForeignKey(Questions, related_name="questions", on_delete=models.DO_NOTHING)
    rating = models.IntegerField(default=0, verbose_name="user's answer rating")

    def __str__(self):
        return self.username

class Questions(models.Model):

    # id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=250, verbose_name=_("Title"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name =_("Date Created"))


    def __str__(self):
        return self.title




class Answers(models.Model):
    questions = models.ForeignKey(Questions, related_name='answers',on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length = 255, verbose_name=_("Answer Text"))
    likes = models.IntegerField(default=0,verbose_name=_("total likes"))
    dislikes = models.IntegerField(default=0,verbose_name=_("total dislikes"))
    byUser = models.ForeignKey(ByUser, verbose_name=_("answered by"), on_delete= models.DO_NOTHING)

    getanswer = PostManager()

    def __str__(self):
        return str(self.likes)

    # def get_absolute_url(self):
    #     return

    # def get_update_url(self):
    #     return     

    # def answerBy(self,questions):
    #     return self.byUser.answerBy(questions)    


# class ByUser(models.Model):
#     username = models.CharField(max_length=100, verbose_name="username")
#     answers =models.ManyToManyField(Answers, related_name="answers")
#     questions = models.ForeignKey(Questions, related_name="questions", on_delete=models.DO_NOTHING)
#     rating = models.IntegerField(default=0, verbose_name="user's answer rating")

#     def __str__(self):
#         return self.username



