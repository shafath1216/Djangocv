from django.db import models

# Create your models here.
class CV(models.Model):
  name=models.CharField(max_length=255)
  address=models.CharField(max_length=255)
  education=models.TextField(max_length=255)
  previous_experience=models.TextField(max_length=255)
  image=models.ImageField(upload_to='photo/', blank=True, null=True)

  def __str__(self):
   return self.name
  