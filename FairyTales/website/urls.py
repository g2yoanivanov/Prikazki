from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tales', views.tales, name='tales'),
    path('authors', views.authors, name='authors'),
    path('<int:id>', views.content, name='content'),

]
