from ast import Return
from importlib.resources import contents
from django.shortcuts import render
from django.shortcuts import View 

# Create your views here.
class BlogListView(View):
  def get(self, request, *args, **kwargs):
      contents={
          
      }
      return render(request, 'blog_list.html', context)
