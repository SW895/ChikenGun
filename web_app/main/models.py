from django.db import models

# Create your models here.
class ArchiveVideo(models.Model):
    date_created = models.DateTimeField(unique=True, blank=False)
    video = models.FileField(upload_to='videos_uploaded', null=True)
    #camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
