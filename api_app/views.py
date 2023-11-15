from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .custompermissions import *

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]