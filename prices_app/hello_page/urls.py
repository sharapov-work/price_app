
from django.urls import path, include
from .views import Hello, Rules, Log_view, enter
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', enter),
    path('login', Log_view.as_view()),
    path('hello', Hello.as_view()),
    path('rules', Rules.as_view()),
    path("logout", LogoutView.as_view(), name="logout"),
]
