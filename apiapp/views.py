from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import ListAPIView
from .mypagination import MyPaginationClass
# Create your views here.
 
 
class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    pagination_class = MyPaginationClass
     