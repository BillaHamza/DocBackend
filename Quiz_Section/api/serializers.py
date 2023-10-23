from Quiz_Section.models import *
from rest_framework import serializers

class SousModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SousModule
        fields = ['id','name','module','courses']

class ModuleSerializer(serializers.ModelSerializer):


    class Meta:
        model = Module
        fields = ['id','name','semestre','sous_modules','modulequizzes','image']



class CoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cours
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class ModuleQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleQuiz
        fields = '__all__'


class SMQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMQuiz
        fields = '__all__'


class CoursQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursQuiz
        fields = '__all__'


class CasCliniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasClinique
        fields = '__all__'


class ExamInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamInfo
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id','text','Qcorrection','Qtype','examInfo','choix','quizzes','scenario','ordre']


class ReponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reponse
        fields = '__all__'


class CommentaireQSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentaireQ
        fields = '__all__'


class SavedQSerializer(serializers.ModelSerializer):
    #questions = serializers.ListField(child=serializers.IntegerField(), write_only=True)

    class Meta:
        model = SavedQ
        fields = '__all__'


class ReponseEtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReponseEtudiant
        fields = '__all__'

class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = ['id','desc','questions']