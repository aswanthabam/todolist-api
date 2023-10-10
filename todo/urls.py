from django.urls import path, include
from .views import *
from rest_framework import routers 
router = routers.SimpleRouter() 

router.register(r'auth/register', UserRegistrationView, basename="User Registration") 
  
urlpatterns = [
    #path('auth/token', ObtainTokenView.as_view()),
    path('',include(router.urls)),
    path('auth/token',ObtainTokenView.as_view())
]