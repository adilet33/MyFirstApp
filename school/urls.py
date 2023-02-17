from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('teachers/', views.teachers, name="teachers"),
    path('schools/', views.schoolname, name="schools"),
    path('register/', views.register, name="register"),
    path('login/', views.loginUser, name="login"),
    path('logout', views.loginout, name="logout"),
    path('create/', views.create, name="create"),
    path('update<str:pk>/', views.update, name="update"),
    path('delete<str:pk>/', views.delete, name="delete"),
]