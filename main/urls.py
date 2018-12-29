from django.urls import path
from . import views
from .views import CorpView, PostView

app_name = 'main'
urlpatterns = [
	path('corp/<int:id>/edit/', CorpView.as_view(), name='corp_edit'),
	path('news/new_post/', PostView.as_view(), name='post_new'),
	path('news/<int:id>/edit/', PostView.as_view(), name='post_edit'),
	path('news/<int:id>/delete/', PostView.as_view(), name='post_delete'),
    path('', views.index, name='index'),
    path('news/<int:post_id>/', views.detail, name='detail'),
    path('news/', views.news, name='news'),
]
