from django.db import models

# Create your models here.
class info_one(models.Model):
    info = models.TextField()

    class Meta:
        verbose_name = "Info1"
        verbose_name_plural = "Info1"

    def __str__(self):
        return self.info
    

class info_two(models.Model):
    info = models.TextField()

    class Meta:
        verbose_name = "Info2"
        verbose_name_plural = "Info2"

    def __str__(self):
        return self.info