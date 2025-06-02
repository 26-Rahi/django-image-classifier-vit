from django.urls import path
from .views import upload_and_classify
from .import views

urlpatterns = [
    path('', upload_and_classify, name='upload'),
    path('confusion-matrix/', views.show_confusion_matrix, name='confusion_matrix'),
]