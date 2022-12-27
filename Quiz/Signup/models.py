from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),

)


class registration_detail(models.Model):
    name = models.CharField(max_length=255)
    School = models.CharField(max_length=255,blank=False)
    standard = models.IntegerField()
    city_of_residence = models.CharField(max_length=255,blank=False)
    
   

   

class Questions(models.Model):

    question = models.FileField(upload_to='',)
    # question = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)



    # def_str_(self):
    #     return str(self.question)


class Answer(models.Model):
    O1 = models.CharField(max_length=255)
    O1 = models.CharField(max_length=255)
    O1 = models.CharField(max_length=255)
    O1 = models.CharField(max_length=255)
    question=models.ForeignKey(Questions, on_delete=models.CASCADE)

    # def_str_(self):
    #     return self.user.username