# username and password -- admin
# username for user-- user@1 and password is geekyshows
# username for user-- admin@ and password is geekyshows
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
# Create your views here.

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    #permission_classes = [AllowAny]
    permission_classes = [IsAdminUser]



    
    