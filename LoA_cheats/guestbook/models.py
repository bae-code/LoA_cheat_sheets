from django.db import models

# Create your models here.
class GuestbookModel(models.Model):
    class Meta:
        db_table = "guestbook"
    
    author = models.CharField(max_length=20, default='모코코')
    content = models.CharField(max_length=100, default='')
    created_date = models.DateField(auto_now_add=True)