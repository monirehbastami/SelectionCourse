from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

from colleges.models import Colleges, Expertises, Hindexs, Majores


class Users(AbstractUser):
    user_code = models.CharField(max_length=30,verbose_name='کد')
    phone_number = models.CharField(max_length=11,verbose_name='شماره تماس')
    mobile = models.CharField(max_length=11,verbose_name='موبایل')
    national_id = models.CharField(max_length=10,verbose_name='کدملی')
    GENDER_CHOICES = [
        (True, 'آقا'),
        (False, 'خانم'),
    ]
    gender = models.BooleanField(choices=GENDER_CHOICES, verbose_name='جنسیت')
    birthdate = models.DateField(verbose_name='تاریخ تولد')
    role = models.ManyToManyField(
        'users.Rols',
        related_name='roles'
    )
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_set_group',
        related_query_name='user_group'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_set_permission',
        related_query_name='user_permission'
    )


class Rols(models.Model):
    title = models.CharField(max_length=30)


class Students(Users):
    user_id = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='student')
    #sal va term ro nemidoonam; agar mohasebat nadarim char bashe
    entry_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(2000),
            MaxValueValidator(2100)
        ]
    )
    entry_semister = models.PositiveIntegerField()
    gpa = models.FloatField(verbose_name='معدل')
    MILITARY_SERVICE_CHOICES = [
        ('completed', 'تکمیل شده'),
        ('exempt', 'معاف'),
        ('deferred', 'معوق'),
        ('in_progress', 'در حال انجام'),
    ]
    military_service_status = models.CharField(max_length=20, choices=MILITARY_SERVICE_CHOICES)
    #سنوات نمیدونم چیه و چطور محاسبه میشه شاید بشه از فیلدای دیگه محاسبش کرد و متد درنظرش گرفت
    academic_years = models.CharField(max_length=4,verbose_name='سنوات')
    majore = models.ForeignKey(Majores,on_delete=models.PROTECT, related_name='student_majore')
    college = models.ForeignKey(Colleges,on_delete=models.PROTECT,related_name='student_college')


class Teachers(Users):
    majore = models.ForeignKey(Majores,on_delete=models.PROTECT, related_name='teacher_majore')
    college = models.ForeignKey(Colleges,on_delete=models.PROTECT,related_name='teacher_college')
    expertise = models.ForeignKey(Expertises,on_delete=models.PROTECT,related_name='teacher_expertise')
    hindex = models.ForeignKey(Hindexs,on_delete=models.PROTECT,related_name='teacher_hindex')