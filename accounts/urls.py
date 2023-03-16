from django.urls import path,include
from accounts.views import login_page,register_page

app_name = 'accounts'

urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
]