from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .serializers import TeacherSerializer, CategorySerializer, CourseSerializer, ChapterSerializer,StudentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

from . import models
# Create your views here.


class TeacherList(generics.ListCreateAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer


@csrf_exempt
def teacher_login(request):
    email = request.POST['email']
    password = request.POST['password']
    try:
        teacherData = models.Teacher.objects.get(
            email=email, password=password)
    except models.Teacher.DoesNotExist:
        teacherData = None
    if teacherData:
        return JsonResponse({'bool': 'True', 'teacher_id': teacherData.id})
    else:
        return JsonResponse({'bool': 'False'})


class CategoryList(generics.ListCreateAPIView):
        queryset = models.CourseCategory.objects.all()
        serializer_class = CategorySerializer


class CourseList(generics.ListCreateAPIView):
        queryset = models.Courses.objects.all()
        serializer_class = CourseSerializer

        def get_queryset(self):
            qs = super().get_queryset()
            if 'result' in self.request.GET:
                 limits= int(self.request.GET['result'])
                 qs = models.Courses.objects.all().order_by('-id')[:limits]
            return qs
class CourseDetailView(generics.RetrieveAPIView):
     queryset=models.Courses.objects.all()
     serializer_class=CourseSerializer

class ChapterList(generics.ListCreateAPIView):
        queryset=models.Chapter.objects.all()
        serializer_class=ChapterSerializer
  
class TeacherCourseList(generics.ListCreateAPIView):
        serializer_class=CourseSerializer
        def get_queryset(self):
            teacher_id =self.kwargs['teacher_id']
            teacher=models.Teacher.objects.get(pk=teacher_id)
            return models.Courses.objects.filter(teacher=teacher)
        
          
class TeacherCourseDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset=models.Courses.objects.all()
        serializer_class=CourseSerializer
 
  

class CourseChapterList(generics.ListAPIView):
        serializer_class=ChapterSerializer
        def get_queryset(self):
            course_id =self.kwargs['course_id']
            course=models.Courses.objects.get(pk=course_id)
            return models.Chapter.objects.filter(course=course)
        


class ChapterDetailView(generics.RetrieveUpdateDestroyAPIView):
     queryset=models.Chapter.objects.all()
     serializer_class=ChapterSerializer


#student data

class StudentList(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer

@csrf_exempt
def student_login(request):
    email = request.POST['email']
    password = request.POST['password']
    try:
        studentData = models.Student.objects.get(
            email=email, password=password)
    except models.Student.DoesNotExist:
        studentData = None
    if studentData:
        return JsonResponse({'bool': 'True', 'teacher_id': studentData.id})
    else:
        return JsonResponse({'bool': 'False'})
