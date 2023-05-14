from django.db import models

class DetectedFace(models.Model):
    image = models.ImageField(upload_to='detected_faces/')
    top = models.IntegerField()
    left = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return f"Detected Face {self.pk}"
