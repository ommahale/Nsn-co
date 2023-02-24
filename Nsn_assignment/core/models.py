from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class Client(models.Model):
    name=models.CharField(max_length=255)
    user_instance=models.ForeignKey(User,on_delete=models.CASCADE,related_name='client')
    def __str__(self) -> str:
        return self.name

class Work(models.Model):
    CHOICES=( ('youtube','youtube'),('instagram','instagram'),('other','other'))
    link=models.URLField()
    work_type=models.CharField(choices=CHOICES,max_length=20,default='youtube')

class Artist(models.Model):
    name=models.CharField(max_length=30)
    works=models.ManyToManyField(Work,related_name='work')
    def __str__(self) -> str:
        return self.name


@receiver(post_save,sender=User)
def user_create_handler(instance,*args,**kwargs):
    Client.objects.create(name=instance.username,user_instance=instance)