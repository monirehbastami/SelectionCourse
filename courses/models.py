from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from colleges.models import Colleges
from users.models import Students, Teachers

# Create your models here.
class CourseKind(models.Model):
    title = models.CharField(max_length=50)

    
class Semesters(models.Model):
    title = models.CharField(max_length=100)
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(2000),
            MaxValueValidator(2100)
        ]
    )
    start_unitselection_date = models.DateField(verbose_name='تاریخ شروع انتخاب واحد')
    end_unitselection_date = models.DateField(verbose_name='تاریخ پایان انتخاب واحد')
    start_classes_date = models.DateField(verbose_name='تاریخ شروع کلاس ها')
    end_classes_date = models.DateField(verbose_name='تاریخ پایان کلاس ها')
    start_unitmodify_date = models.DateField(verbose_name='تاریخ شروع حذف و اضافه')
    end_unitmodify_date = models.DateField(verbose_name='تاریخ پایان حذف و اضافه')
    end_emergency_date = models.DateField(verbose_name='تاریخ پایان حذف اضطراری')
    start_exam_date = models.DateField(verbose_name='تاریخ شروع امتحانات')
    end_exam_date = models.DateField(verbose_name='تاریخ پایان امتحانات')
    
class CourseStatus(models.Model):
    title = models.CharField(max_length=100)


class Courses(models.Model):
    title = models.CharField(max_length=100)
    prerequisites = models.ManyToManyField('self', blank=True)
    postrequisites = models.ManyToManyField('self', blank=True)
    unit_number = models.PositiveIntegerField()
    course_kind  = models.ForeignKey(CourseKind,on_delete=models.PROTECT,related_name='coursekind')    
    college = models.ForeignKey(Colleges,on_delete=models.PROTECT,related_name='course_college')
    semester = models.ManyToManyField(Semesters,  blank=True,related_name='course_semester')
    teacher = models.ManyToManyField(Teachers,  blank=True,related_name='course_teacher')
    student = models.ManyToManyField(Students,  blank=True,related_name='course_student')
    course_score = models.PositiveIntegerField()
    course_status =  models.ForeignKey(CourseStatus,on_delete=models.PROTECT,related_name='course_status')    
    capacity = models.PositiveIntegerField()
    exam_date = models.DateField(verbose_name='تاریخ شروع امتحان')
    exam_place = models.CharField(max_length=50,verbose_name='مکان امتحان')

    def __str__(self):
        return self.name



