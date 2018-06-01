from django.db import models
from django.contrib.auth.models import User
# from DjangoUeditor.models import UEditorField
# Create your models here.

class BlogsPost(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	timestemp = models.DateTimeField()


class Category(models.Model):
	name = models.CharField(max_length=100)


class Tag(models.Model):
	name = models.CharField(max_length=100)


class Post(models.Model):
	title = models.CharField(max_length=70)
	body = models.TextField()
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	excerpt = models.CharField(max_length=200,blank=True)
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag,blank=True)
	author = models.ForeignKey(User,on_delete=models.CASCADE)



	
# Content = UEditorField(u'内容 ',width=600, height=300, toolbars="full", imagePath="templates/images", filePath="templates/files", 
# 						upload_settings={"imageMaxSize":1204000},blank=True)