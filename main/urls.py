# user_management/urls.py
from django.urls import path
from .views import signup, login_view, dashboard

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('/login/', login_view, name='login'),
    # path('dashboard/', dashboard, name='dashboard'),   
    path('dashboard/<str:user_type>/', dashboard, name='dashboard'),

    path('', signup, name='signup'),
   
]
