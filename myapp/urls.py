from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('<lang_code>/', views.switch_language, name='switch_language'),
    ]
