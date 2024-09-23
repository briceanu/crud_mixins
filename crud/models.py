from django.db import models
import uuid
# Create your models here.

class Book(models.Model):
    book_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False) 
    name = models.CharField(max_length=30,null=False,unique=True)
    author = models.CharField(max_length=30, null=False)
    year_of_publish = models.SmallIntegerField(null=False)
