from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=33,null=True,blank=True)
    email=models.EmailField()
    message=models.CharField(null=True,blank=True,max_length=400)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__ (self):
        return self.name