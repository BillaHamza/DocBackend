from rest_framework.permissions import BasePermission
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class CustomBaseView(APIView):
    permission_classes = [IsAuthenticated] 



class IsAuthorCP(BasePermission):

    def has_object_permission(self, request, view, obj):
        # Allow read (GET) requests for all users
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True

        # Check if the user is authenticated and is the author of the CommentaireQ or Post .....
        return request.user == obj.etudiant



class IsAuthor(BasePermission):
 
    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated and is the author of SavedQ or ReponsesEtudiant ....
        return request.user == obj.etudiant