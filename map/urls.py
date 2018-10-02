from django.urls import path

from . import views

app_name = 'map'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:field_id>/', views.detail, name='detail')
]
