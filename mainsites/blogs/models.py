from django.db import models

class Blog(models.Model):
    blogid = models.IntegerField(**null=True**)
    blogtitle = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    blogcontent = models.TextField()
    blogdesc = models.CharField(max_length=256)
    createtime = models.DateTimeField(auto_now_add=True)
    lastchagetime = models.DateTimeField(auto_now=True)
    creartor = models.CharField(max_length=50)

class MyUser(models.Model):
    userid = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    age = models.IntegerField() 
