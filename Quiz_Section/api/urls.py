from django.urls import path
from Quiz_Section.api import views


urlpatterns = [
    # GET endpoints
    path('module/', views.ModuleList.as_view()),
    path('sousmodule/', views.SousModuleList.as_view()),
    path('cours/', views.CoursList.as_view()),
    path('quiz/', views.QuizList.as_view()),
    path('modulequiz/', views.ModuleQuizList.as_view()),
    path('smquiz/', views.SMQuizList.as_view()),
    path('coursquiz/', views.CoursQuizList.as_view()),
    path('casclinique/', views.CasCliniqueList.as_view()),
    path('scenario/', views.ScenarioList.as_view()),

    path('examinfo/', views.ExamInfoList.as_view()),
    path('question/', views.QuestionList.as_view()),
    path('reponse/', views.ReponseList.as_view()),

    # GET / POST endpoints
    path('reponseetudiant/', views.ReponseEtudiantList.as_view()),
    path('commentaireq/', views.CommentaireQList.as_view()),
    path('savedq/', views.SavedQList.as_view()),

    # GET (retrieve one by ID) endpoints
    path('module/<int:pk>/', views.ModuleDetail.as_view()),
    path('sousmodule/<int:pk>/', views.SousModuleDetail.as_view()),
    path('cours/<int:pk>/', views.CoursDetail.as_view()),
    path('quiz/<int:pk>/', views.QuizDetail.as_view()),
    path('modulequiz/<int:pk>/', views.ModuleQuizDetail.as_view()),
    path('smquiz/<int:pk>/', views.SMQuizDetail.as_view()),
    path('coursquiz/<int:pk>/', views.CoursQuizDetail.as_view()),
    path('casclinique/<int:pk>/', views.CasCliniqueDetail.as_view()),
    path('scenario/<int:pk>/', views.ScenarioDetail.as_view()),
    path('examinfo/<int:pk>/', views.ExamInfoDetail.as_view()),
    path('question/<int:pk>/', views.QuestionDetail.as_view()),
    path('reponse/<int:pk>/', views.ReponseDetail.as_view()),

    # PUT and DELETE endpoints for specific models
    path('commentaireq/<int:pk>/', views.CommentaireQDetail.as_view()),
    path('savedq/<int:pk>/', views.SavedQDetail.as_view()),
    path('reponseetudiant/<int:pk>/', views.ReponseEtudiantDetail.as_view()),
]