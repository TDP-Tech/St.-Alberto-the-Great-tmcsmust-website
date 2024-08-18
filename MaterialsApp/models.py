from django.db import models

class StudyMaterial(models.Model):
    title = models.CharField(max_length=100)
    level = models.CharField(max_length=50, choices=[
        ('Certificate', 'Certificate'),
        ('Diploma', 'Diploma'),
        ('Bachelor Degree', 'Bachelor Degree'),
        ('Masters', 'Masters'),
        ('Doctor of Philosophy', 'Doctor of Philosophy'),
    ])
    course = models.CharField(max_length=200)
    year_of_study = models.IntegerField(default=0000)
    date_posted = models.DateField()
    document = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.title
