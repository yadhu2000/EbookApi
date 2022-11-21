from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import json

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

#for authentication---------------------------

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

#----------------------------------------------

# details for book design-------------------------------
class Ebooks(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=500)
    Author = models.CharField(max_length=500)
    Genre = models.CharField(max_length=500)
    def set_foo(self, x):
        self.Genre = json.dumps(x)

    def get_foo(self):
        return json.loads(self.Genre)
    Review = models.PositiveIntegerField(validators=[MinValueValidator(1), MinValueValidator(5)])
    Favorite = models.BooleanField(default=True)


    #-----------------------------------------------------
    