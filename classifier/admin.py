from django.contrib import admin
from .models import UploadedImage

@admin.register(UploadedImage)
class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'predicted_label', 'true_label', 'uploaded_at')
    list_editable = ('true_label',)