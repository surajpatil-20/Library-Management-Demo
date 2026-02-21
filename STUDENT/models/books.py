from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=20)
    auther = models.CharField(max_length=100)
    total_copies = models.IntegerField()
    avail_copies = models.IntegerField()

    def __str__(self):
        return f"{self.id} {self.title} {self.auther} {self.total_copies} {self.avail_copies}\n" 
    


