from django.urls import path
from .views import *
urlpatterns = [
    path('',adminpage, name='homes'),
    path('signup/', SignUpView.as_view(), name='signup'),
]