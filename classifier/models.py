from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    true_label = models.CharField(max_length=100, blank=True, null=True)
    predicted_label = models.CharField(max_length=100, blank=True, null=True)

    def _str_(self):
        return self.image.name