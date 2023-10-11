from django.urls import path, include
from .views import *
from rest_framework import routers 

urlpatterns = [
    #path('auth/token', ObtainTokenView.as_view()),
    path('auth/register/',UserRegistrationView.as_view()),
    path('auth/token/',ObtainTokenView.as_view()),
    path('tasks/add/',TaskAddView.as_view()),
    path('tasks/',TaskGetView.as_view()),
    path('tasks/complete/',TaskMarkCompleted.as_view()),
    path('tasks/edit/',TaskEditView.as_view()),
    path('tasks/delete/',TaskDeletion.as_view())
]