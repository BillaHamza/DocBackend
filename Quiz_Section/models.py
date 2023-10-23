from django.db import models
from Accounts.models import Semestre,CustomUser


class Module(models.Model):
    name = models.CharField(max_length=400)
    semestre = models.ForeignKey(Semestre, on_delete=models.SET_NULL,null=True,related_name="modules")
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name + " " + self.semestre.name

class SousModule(models.Model):
    name = models.CharField(max_length=400)
    module = models.ForeignKey(Module, on_delete=models.CASCADE,related_name="sous_modules")
    
    def __str__(self):
        return self.name

class Cours(models.Model):
    name = models.CharField(max_length=400)
    sous_module = models.ForeignKey(SousModule, on_delete=models.CASCADE,related_name="courses")
    #module = models.ForeignKey(Module, on_delete=models.CASCADE,related_name="courses")

    def __str__(self):
        return self.name


class Quiz(models.Model):
    questions = models.ManyToManyField('Question', related_name="quizzes", blank=True)
    scenarios = models.ManyToManyField('Scenario',related_name="quizzes",blank=True)
    nbreQuestions = models.IntegerField(default=50)


class ModuleQuiz(Quiz):
    module = models.ForeignKey(Module, on_delete=models.CASCADE,related_name="modulequizzes")
    examinfo = models.ForeignKey('ExamInfo',null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.module.name + " - " + self.examinfo.annee + " - " + self.examinfo.session


class SMQuiz(Quiz):
    sousModule = models.ForeignKey(SousModule, on_delete=models.CASCADE)
    examinfo = models.ForeignKey('ExamInfo',null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.sousModule.name + " - " + self.examinfo.annee

class CoursQuiz(Quiz):
    cours = models.OneToOneField(Cours,on_delete=models.CASCADE)
    def __str__(self):
        return self.cours.name + " -- Quiz " 


class CasClinique(Quiz):
    module = models.OneToOneField(Module, on_delete=models.CASCADE)
    def __str__(self):
        return self.module.name

class Scenario(models.Model):
    desc = models.TextField()

    def __str__(self):
        return self.desc[:50]



###For every field that has choices set, the object will have a get_FOO_display() method, where FOO is the name of the field.
# This method returns the “human-readable” value of the field.


class ExamInfo(models.Model):
    sessionChoices = [("NL","Normal"),
                  ("RAT","Rattrapage"),
                  ("EXP","Exceptionnel"),
                 ]
    examCorrect = [("Off" , "Officiel"),
                   ("Col","Collective"),
                   ("Non","Non Disponible"),
                ]
    
    session = models.CharField(choices=sessionChoices,max_length=3)
    annee = models.CharField(max_length=4)
    correction = models.CharField(choices=examCorrect,max_length=3)
    
    def __str__(self):
        return self.session + " " + self.annee



class Question(models.Model):
    QuestChoice = [("Mult","Multiple"),("text","Ordonnance & CROC"), ("img","Dessin")]
    text = models.TextField()
    Qcorrection = models.BooleanField(default=True)
    Qtype = models.CharField(choices=QuestChoice,max_length=4)
    examInfo = models.ForeignKey(ExamInfo, on_delete=models.SET_NULL,null=True)
    scenario= models.ForeignKey(Scenario,on_delete=models.SET_NULL,null=True,related_name="questions",blank=True)
    ordre = models.PositiveSmallIntegerField() 

    class Meta:
        ordering = ['ordre']
        
    def __str__(self):
        return self.text[:50]


class Note(models.Model):
    etudiant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    notes = models.TextField()



class Reponse(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name="choix")
    text = models.TextField(blank=True)
    is_correct = models.BooleanField(default=False)
    image = models.ImageField(null=True,blank=True)
    ordre = models.CharField(max_length=1)

    class Meta:
        ordering = ['ordre']

    def __str__(self):
        return self.text[:50]



class CommentaireQ(models.Model):
    etudiant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:50]


class SavedQ(models.Model):
    etudiant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.SET_NULL,null=True)
    sous_module = models.ForeignKey(SousModule, on_delete=models.SET_NULL,null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        ordering = ['question']

class ReponseEtudiant(models.Model):
    etudiant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    rep = models.ManyToManyField(Reponse)




