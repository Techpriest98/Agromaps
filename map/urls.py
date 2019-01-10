from django.urls import path
from . import views
from .views import FieldsListView, CultureListView, SeedListView, SeedView, FieldView, CultureView

app_name = 'map'
urlpatterns = [
    path('', views.index, name='index'),
    #Field routes
    path('fields/', views.fields, name='fields'),
    path('fields/map/', FieldsListView.as_view(), name='map-api'),
    #Culture routes
    path('cultures/', views.cultures, name='cultures'),
    path('cultures/<int:culture_id>/edit/', CultureView.as_view(), name='culture_edit'),
     path('new_culture/', CultureView.as_view(), name='culture_new'),

    path('<int:seed_id>/', views.detail, name='detail'),
    path('new_seed/', SeedView.as_view(), name='seed_new'),
    path('fields/<int:seed_id>/edit/', SeedView.as_view(), name='seed_edit'),

    path('new_field/', FieldView.as_view(), name='field_new'),
    path('new_field/map/', FieldsListView.as_view(), name='map-api'),
    path('map/', FieldsListView.as_view(), name='map-api'),
    path('culture/', CultureListView.as_view(), name='culture-api'),
    path('seed/', SeedListView.as_view(), name='seed-api'),
    path('new_seed/map/', FieldsListView.as_view(), name='map-api'),
    path('new_seed/culture/', CultureListView.as_view(), name='culture-api'),
    path('new_seed/seed/', SeedListView.as_view(), name='seed-api')
]
