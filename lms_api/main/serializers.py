from rest_framework import serializers
from . import models


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['id','detail','full_name', 'email', 'password',
                  'qualification', 'mobile_no', 'skills','teacher_courses']
        depth=1
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id','full_name', 'email', 'password',
                  'username','interested_categories']
        depth=1

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ['id', 'title', 'description']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Courses
        fields = ['id', 'category', 'teacher', 'title',
                  'description', 'featured_img', 'techs','course_chapters','related_videos','tech_list']
        depth=1

        # depth helps find detail of depth

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chapter
        fields = ['id', 'course', 'title',
                  'description', 'video', 'remarks']
