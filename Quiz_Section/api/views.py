from Quiz_Section.models import * 
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from .permissions import *
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.http import Http404



# from rest_framework.permissions import IsAuthenticated

# from rest_framework_simplejwt.authentication import JWTAuthentication







#------------------------------------GET[Many] / POST -----------------------------------#



class ModuleList(generics.ListAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    def get_queryset(self):
        semestre_id = self.request.query_params.get('semestre')
        if semestre_id:
            return Module.objects.filter(semestre=semestre_id)
        return Module.objects.all()

class SousModuleList(generics.ListAPIView):
    queryset = SousModule.objects.all()
    serializer_class = SousModuleSerializer
    def get_queryset(self):
        module_id = self.request.query_params.get('module')
        if module_id:
            return SousModule.objects.filter(module=module_id)
        return SousModule.objects.all()

class CoursList(generics.ListAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer
    def get_queryset(self):
        sous_module_id = self.request.query_params.get('sous_module')
        if sous_module_id:
            return Cours.objects.filter(sous_module=sous_module_id)
        return Cours.objects.all()

class QuizList(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class ModuleQuizList(generics.ListAPIView):
    queryset = ModuleQuiz.objects.all()
    serializer_class = ModuleQuizSerializer
    def get_queryset(self):
        module_id = self.request.query_params.get('module')
        if module_id:
            return ModuleQuiz.objects.filter(module=module_id)
        return ModuleQuiz.objects.all()

class SMQuizList(generics.ListAPIView):
    queryset = SMQuiz.objects.all()
    serializer_class = SMQuizSerializer
    def get_queryset(self):
        sousModule_id = self.request.query_params.get('sousModule')
        if sousModule_id:
            return SMQuiz.objects.filter(sousModule=sousModule_id)
        return SMQuiz.objects.none()

class CoursQuizList(generics.ListAPIView):
    queryset = CoursQuiz.objects.all()
    serializer_class = CoursQuizSerializer

class CasCliniqueList(generics.ListAPIView):
    queryset = CasClinique.objects.all()
    serializer_class = CasCliniqueSerializer

class ScenarioList(generics.ListAPIView):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer

    def get_queryset(self):
        ids = self.request.query_params.get('id')
        if ids:
            ids_list = [int(id) for id in ids.split(',') if id.isdigit()]
            return Scenario.objects.filter(id__in=ids_list)
        return Scenario.objects.all()

class ExamInfoList(generics.ListAPIView):
    queryset = ExamInfo.objects.all()
    serializer_class = ExamInfoSerializer

    def get_queryset(self):
        ids = self.request.query_params.get('id')
        if ids:
            ids_list = [int(id) for id in ids.split(',') if id.isdigit()]
            return ExamInfo.objects.filter(id__in=ids_list)
        return ExamInfo.objects.all()

class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        ids = self.request.query_params.get('id')
        if ids:
            ids_list = [int(id) for id in ids.split(',') if id.isdigit()]
            return Question.objects.filter(id__in=ids_list).order_by('id')
        return Question.objects.all().order_by('id')

class ReponseList(generics.ListAPIView):
    queryset = Reponse.objects.all()
    serializer_class = ReponseSerializer
    def get_queryset(self):
        question_id = self.request.query_params.get('question')
        if question_id:
            return Reponse.objects.filter(question=question_id)
        return Reponse.objects.all()

class ReponseEtudiantList(generics.ListCreateAPIView):
    queryset = ReponseEtudiant.objects.all()
    serializer_class = ReponseEtudiantSerializer

class CommentaireQList(generics.ListCreateAPIView):
    queryset = CommentaireQ.objects.all()
    serializer_class = CommentaireQSerializer

class SavedQList(generics.ListCreateAPIView):
    serializer_class = SavedQSerializer
    def get_queryset(self):
        user_id = self.request.query_params.get('etudiant')
        questions = self.request.query_params.get('question')
        module_id = self.request.query_params.get('module') 

        if module_id and user_id:
            return SavedQ.objects.filter(etudiant=user_id, module=module_id).order_by('id')
        elif questions and user_id:
            questions_list = [int(id) for id in questions.split(',') if id.isdigit()]
            return SavedQ.objects.filter(etudiant=user_id, question__in=questions_list).order_by('id')

        return SavedQ.objects.all().order_by('id')
    

    def create(self, request, *args, **kwargs):
        # Check if the request data is a list (multiple SavedQ objects)
        if isinstance(request.data, list):
            saved_qs = []
            for item in request.data:
                serializer = self.get_serializer(data=item)
                serializer.is_valid(raise_exception=True)
                saved_qs.append(SavedQ(**serializer.validated_data))
            # Bulk insert the saved_qs
            SavedQ.objects.bulk_create(saved_qs)
            return Response({"message": "SavedQ records created successfully"}, status=status.HTTP_201_CREATED)
        else:
            # If not a list, use the default create method for single object creation
            return super(SavedQList, self).create(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        # Get a comma-separated list of IDs from the query parameters
        ids = request.query_params.get('id', '')

        # Split the IDs into a list
        ids_list = [int(id) for id in ids.split(',') if id.isdigit()]
            #return SavedQ.objects.filter(etudiant=user_id, question__in=questions_list)

        if not ids_list:
            return Response(
                {"error": "No valid IDs provided for deletion."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Filter the queryset to include only the selected IDs
            savedq_items = self.get_queryset().filter(id__in=ids_list)
            
            if savedq_items.exists():
                # Delete the selected SavedQ items
                savedq_items.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(
                    {"error": "One or more SavedQ items not found."},
                    status=status.HTTP_404_NOT_FOUND
                )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    #permission_classes = [IsAuthor]


#--------------------------------------------------------------------------------------#

#------------------------------------GET (For One) / PUT / DELETE -----------------------------------#

class ModuleDetail(generics.RetrieveAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
   

class SousModuleDetail(generics.RetrieveAPIView):
    queryset = SousModule.objects.all()
    serializer_class = SousModuleSerializer
  

class CoursDetail(generics.RetrieveAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer
    

class QuizDetail(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    

class ModuleQuizDetail(generics.RetrieveAPIView):
    queryset = ModuleQuiz.objects.all()
    serializer_class = ModuleQuizSerializer
   

class SMQuizDetail(generics.RetrieveAPIView):
    queryset = SMQuiz.objects.all()
    serializer_class = SMQuizSerializer
   

class CoursQuizDetail(generics.RetrieveAPIView):
    queryset = CoursQuiz.objects.all()
    serializer_class = CoursQuizSerializer
    

class CasCliniqueDetail(generics.RetrieveAPIView):
    queryset = CasClinique.objects.all()
    serializer_class = CasCliniqueSerializer

class ScenarioDetail(generics.RetrieveAPIView):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer
    

class ExamInfoDetail(generics.RetrieveAPIView):
    queryset = ExamInfo.objects.all()
    serializer_class = ExamInfoSerializer
  

class QuestionDetail(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    

class ReponseDetail(generics.RetrieveAPIView):
    queryset = Reponse.objects.all()
    serializer_class = ReponseSerializer


class CommentaireQDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentaireQ.objects.all()
    serializer_class = CommentaireQSerializer
    permission_classes = [IsAuthorCP]

class SavedQDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SavedQ.objects.all()
    serializer_class = SavedQSerializer
    #permission_classes = [IsAuthor]

    




class ReponseEtudiantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReponseEtudiant.objects.all()
    serializer_class = ReponseEtudiantSerializer
    permission_classes = [IsAuthor]