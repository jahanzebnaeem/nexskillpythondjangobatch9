from django.shortcuts import render
from django.utils import timezone
from blog.models import Post, Comment
from django.views.generic import TemplateView

# Create your views here.

class AboutView(TemplateView):
    template_name = 'blog/about.html'
