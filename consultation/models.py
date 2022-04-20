from django.db import models
#from django.contrib.auth.models import AbstractUser
from capstone.settings import AUTH_USER_MODEL
#from users.models import User

# Create your models here.
class Consultation(models.Model):
    name = models.CharField(max_length=64, default="")
    consultant = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,
    related_name="consultant_set")
    patient = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,
    related_name="consultation_patient_set", null=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    rating = models.IntegerField(default=0)
    review = models.TextField(max_length=100, default="", blank=True)

    def __str__(self):
        return f'Consultation: Started on {self.start_date}, is active: {self.is_active}'

class Message(models.Model):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE,
     related_name='chat_messages')
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=264)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message: {self.content}, From: {self.user}, on: {self.timestamp}"


