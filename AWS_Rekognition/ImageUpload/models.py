from django.db import models


class ImageUpload(models.Model):
    employee_name = models.CharField(max_length=50)
    Image = models.ImageField(upload_to='images/')


