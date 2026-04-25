from django.urls import path
from login import views as login_views

urlpatterns = [
    path('', login_views.LoginView.as_view(), name='login'),
    path('landing', login_views.landing, name='landing'),
]