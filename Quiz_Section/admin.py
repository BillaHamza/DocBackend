from django.contrib import admin
from .models import *

admin.site.register(Module)
admin.site.register(SousModule)
admin.site.register(Cours)
admin.site.register(Quiz)
admin.site.register(ModuleQuiz)
admin.site.register(SMQuiz)
admin.site.register(CoursQuiz)
admin.site.register(CasClinique)
admin.site.register(Question)
admin.site.register(Reponse)
admin.site.register(ReponseEtudiant)
admin.site.register(SavedQ)
admin.site.register(CommentaireQ)
admin.site.register(ExamInfo)
admin.site.register(Scenario)

