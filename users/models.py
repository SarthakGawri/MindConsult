from django.db import models
#from django.utils import timezone
#from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_consultant = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    qualification = models.CharField(max_length=64)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    groups = models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    related_name='user_group_set', related_query_name='user',
    to='auth.Group', verbose_name='groups')
    user_permissions = models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
    related_name='user_permission_set', related_query_name='user',
    to='auth.Permission', verbose_name='user permissions')

""" class Consultant(models.Model):
    password = models.CharField(max_length=128, verbose_name='password')
    last_login = models.DateTimeField(blank=True, null=True, verbose_name='last login')
    is_superuser = models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')
    username = models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=UnicodeUsernameValidator(), verbose_name='username')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='date joined')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=50)
    #consultations = models.ForeignKey('consultation.Consultation',
    #on_delete=models.CASCADE, related_name="consultation_set", null=True, blank=True)
    avg_rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)

    def __str__(self):
        return f'Consultant: {self.first_name} {self.last_name} {self.qualification}'

class Patient(models.Model):
    password = models.CharField(max_length=128, verbose_name='password')
    last_login = models.DateTimeField(blank=True, null=True, verbose_name='last login')
    is_superuser = models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')
    username = models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=UnicodeUsernameValidator(), verbose_name='username')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='date joined')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #past_consultations = models.ForeignKey('consultation.Consultation',
    #on_delete=models.CASCADE, related_name="past_consultations_set", null=True, blank=True)
    reviews = models.ManyToManyField('Consultant', blank=True)

    def __str__(self):
        return f'Patient: {self.first_name} {self.last_name}' """
