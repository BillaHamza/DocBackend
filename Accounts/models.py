from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager



class Faculte(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Semestre(models.Model):
    name = models.CharField(max_length=5)
    faculte = models.ForeignKey(Faculte,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name




class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    faculte = models.ForeignKey('Faculte',null=True, on_delete=models.SET_NULL)
    semestres = models.ManyToManyField('Semestre',related_name='users',through="Membership")
    quizzes = models.ManyToManyField('Quiz_Section.Quiz', related_name='users',through="ResultatQuiz")
    is_verified = models.BooleanField(default=False)
    is_subscribed = models.BooleanField(default=False)
    avatar = models.ImageField(null=True,default="")
    Genders = [("F", "Female"),("M","Male")]
    sexe = models.CharField(max_length=1, choices=Genders,null=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    


class ResultatQuiz(models.Model):
    etudiant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quiz = models.ForeignKey('Quiz_Section.Quiz', on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    duration = models.IntegerField(null=True)
    is_passed = models.BooleanField(default=False)



class Membership(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    semestre = models.ForeignKey('Semestre', on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)
    PaiementChoices = [("Ch","Cash"),("Carte","Carte"),("Vir","Virement")]
    typePaiement = models.CharField(choices=PaiementChoices,max_length=6)
    end_date = models.DateField()
