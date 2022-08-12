from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Video
import sys

class IndexView(ListView):
    template_name = 'index.html'
    model = Video
    #context_object_name = 'videos'

class ListVideosByCategory(ListView):
    template_name = 'videos_by_category.html'
    def get_queryset(self):
        category_name = self.kwargs['category_name']
        print(category_name)
        queryset = Video.objects.filter(
            category__name__iexact = category_name 
        )
        return queryset
    



    