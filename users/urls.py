from django.urls import path
from users.views import UserHomeView

app_name = 'users'
urlpatterns = [
    path('',UserHomeView.as_view(),name='index'),
]
