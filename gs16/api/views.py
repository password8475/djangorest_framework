# GenericAPIView and Model Mixin

from .models import Student 
from .serializers import StudentSerializer
from rest_framework.generics import  ListCreateAPIView,  RetrieveUpdateDestroyAPIView

# List and Create -- PK Not Required

class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Retrieve Update Destroy -- PK Required
class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer           