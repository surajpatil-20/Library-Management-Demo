from django.db import models
from models.books import Books
from models.member import Member

class BorrowRecord(models.Model):
    member = models.ForeignKey(Member,on_delete = models.CASCADE)
    book = models.ForeignKey(Books,on_delete = models.CASCADE)
    borrowed_date = models.DateField(null=False)
    returned_date = models.DateTimeField(null=True)
    is_returned = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.id} {self.member} has borrowed {self.book} on {self.borrowed_date}\n"
# Create your models here.
