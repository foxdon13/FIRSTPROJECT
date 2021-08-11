from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50,help_text="Enter the name of the project")
    Description = models.TextField(max_length=1000,help_text="Enter the description")
    back_end_technology = models.CharField(max_length=50,verbose_name = "Backend Technology")
    front_end_technology = models.CharField(max_length=50,verbose_name="Frontend Technology")
