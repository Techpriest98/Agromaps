from django.urls import path

from .views import login_view, logout_view

app_name = 'authentication'
urlpatterns = [
    path('login/', login_view),
    path('logout/', logout_view)
]
