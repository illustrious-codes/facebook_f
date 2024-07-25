from django.db import models

class Facebook(models.Model):
    Number = models.CharField(max_length=15, null=False, blank=False)
    Password = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.Number