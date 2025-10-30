from django.db import models

# Create your models here.




class Contact(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=120)
    message = models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'