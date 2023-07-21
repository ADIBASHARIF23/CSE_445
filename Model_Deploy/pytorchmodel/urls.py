from django.urls import path,include
from pytorchmodel import views
urlpatterns = [
    path('record_submission',views.record_submission),
    path('feedback_submission',views.feedback_submission),
    path('',views.home),
]
