from django.db import models
class Member(models.Model):
    name = models.CharField(max_length=50,null=False)
    email = models.EmailField(max_length=50,null=False)
    joined_date = models.DateField()

    def __str__(self):
        return f"{self.id} --> name = {self.name} email = {self.email} joined_date ={self.joined_date}\n"
    
