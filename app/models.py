from django.db import models

# Create your models here.


class Topic(models.Model):
    topics_names=models.CharField(max_length=100,primary_key=True)



class Webpage(models.Model):
    topics_names=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True)
    url=models.URLField()


class AccessRecodes(models.Model):
    names=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()

