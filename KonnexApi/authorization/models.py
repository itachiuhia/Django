# from django.db import models


# # Create your models here.

# # class Register(models.Model):
# #     first_name = models.CharField(max_length=20)
# #     last_name = models.CharField(max_length=20)
# #     email = models.EmailField(max_length=100)
# #     date = models.DateTimeField(auto_now_add=True)

# #     def __str__(self):
# #         return self.first_name+" "+self.last_name


from django.db import models
from faq.models import Questions, Answers

# class Profiles(models.Model):
#       pass


class User_Profile(models.Model):
    username = models.CharField(max_length=200, verbose_name = "username")
    email = models.EmailField(max_length=200, verbose_name = "email")
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    rating = models.IntegerField(default=0)
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answers = models.ForeignKey(Answers, on_delete=models.CASCADE)





    
