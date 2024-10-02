from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app1_home'),  # Ensure this matches what you're referencing
    path('page1/', views.page1, name='app1_page1'),
    path('page2/', views.page2, name='app1_page2'),
]
