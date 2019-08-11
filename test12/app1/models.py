from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=256)
    webaddress=models.URLField(blank=True,null=True)
    cover_letter=models.TextField(blank=True,null=True)
    attachment=models.ImageField(upload_to='images',blank=True,null=True)



    def __str__(self):
        return self.user.username
