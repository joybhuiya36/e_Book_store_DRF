from django.urls import path
from .views import RegisterView

urlpatterns = [
    path('auth/signup/', RegisterView.as_view(), name='signup'),
]
