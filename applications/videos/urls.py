from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('category/<category_name>', views.ListVideosByCategory.as_view()),
]
