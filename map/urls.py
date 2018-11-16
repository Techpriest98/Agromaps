from django.urls import path

from . import views
from .views import FieldsListView, CultureListView, SeedListView

app_name = 'map'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:field_id>/', views.detail, name='detail'),
    path('map/', FieldsListView.as_view(), name='map-api'),
    path('culture/', CultureListView.as_view(), name='culture-api'),
    path('seed/', SeedListView.as_view(), name='seed-api')
]
