from django.db import models

# Create your models here.
class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    current = models.BooleanField(default=False)
    description = models.TextField()

    class Meta:
        ordering = ['-start_date']

        def __str__(self):
            return self.title
        

class Education(models.Model):
    title = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    class Meta:
        ordering = ['-start_date']

        def __str__(self):
            return self.title
        
class Skills(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    earned = models.DateField()
    def __str__(self):
        return self.title
    
class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title