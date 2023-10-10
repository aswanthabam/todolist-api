from django.urls import path, include
from .views import *
from rest_framework import routers 
router = routers.DefaultRouter() 

router.register(r'register', UserRegistrationView) 
  
urlpatterns = [
    path('auth/token', ObtainTokenView.as_view()),
    path('auth/',include(router.urls)),
    path("api",include('rest_framework.urls'))
]